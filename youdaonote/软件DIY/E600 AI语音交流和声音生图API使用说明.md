# ChatBot 客户端使用说明

本文档面向设备端/客户端开发，说明如何与服务端 ChatBot 进行鉴权、建立 WebSocket 连接、上传语音音频并接收 TTS 音频与转写文本。

## 1. 术语与前置条件

- `device_id`：设备唯一标识（服务端已注册）。
- `device_secret`：设备密钥，仅在注册时返回一次，需安全存储在设备端，不可明文上报。
- `nonce`：服务端下发的随机挑战串，缓存 60s，仅能使用一次。
- `signature/sign`：`HMAC_SHA256(device_secret, nonce)` 的十六进制小写字符串。
- `access token`：JWT，包含 `device_id` 等 claim，用于 WS 鉴权。

部署建议：

- 生产环境必须使用 `HTTPS/WSS`。
- 服务端依赖缓存（通常是 Redis）存储 nonce 与用量统计。

## 2. 鉴权流程（必须）

ChatBot WebSocket 连接需要同时提供：

- `token`：JWT access token
- `nonce`：一次性挑战串
- `sign`：对该 nonce 的 HMAC 签名

注意：`/device/token/` 在签发 token 成功后会删除该次 challenge 的 nonce（防重放）。因此建议按如下顺序做两次 challenge：

1. 获取 `token` 用的 challenge
2. 获取 WS 连接用的 challenge

### 2.1 获取 access/refresh token（Challenge-Response）

两步 challenge-response（避免明文传输 `device_secret`）：

1) 请求 nonce（challenge）

`POST /device/challenge/`

请求：
```json
{ "device_id": "LYY-202603-000123" }
```

响应：
```json
{ "nonce": "..." }
```

2) 计算签名并换取 token

- 在设备端计算 `signature = HMAC_SHA256(device_secret, nonce)` 并输出 hex（`device_secret` 不上送）。

在设备端计算：

`signature = hex(HMAC_SHA256(key=device_secret, msg=nonce))`

`POST /device/token/`

请求：
```json
{ "device_id": "LYY-202603-000123", "signature": "<hex-hmac-sha256>" }
```

响应：
```json
{ "access": "<access_jwt>", "refresh": "<refresh_jwt>" }
```

补充：

- nonce 在服务端缓存时间很短（约 60s），且成功使用后会被删除；过期或已使用需要重新获取 nonce。

### 2.2 刷新 access token（SimpleJWT 标准接口）

access token 过期后，使用 refresh token 换取新的 access：

`POST /api/token/refresh/`

请求：
```json
{ "refresh": "<refresh_token>" }
```

响应：
```json
{ "access": "<new_access_token>" }
```

### 2.3 获取 WS 连接用的 nonce/sign（每次连接前都做一次）

在每次发起 WebSocket 连接之前，再调用一次：

`POST /device/challenge/` -> 得到 `nonce_ws`

在设备端计算：

`sign_ws = hex(HMAC_SHA256(key=device_secret, msg=nonce_ws))`

随后用 `access token + nonce_ws + sign_ws` 建立 WS 连接（见下一节）。

## 3. WebSocket 连接信息

### 3.1 连接地址

路径（服务端路由固定）：

- `GET /ws/chatbot/`

连接 URL（示例）：

`wss://<host>/ws/chatbot/?token=<access>&nonce=<nonce_ws>&sign=<sign_ws>`

### 3.2 语言选项参数（`lang`）

语言选项通过 **Query String** 附加在 WebSocket URL 末尾，在建立连接时一次性传入，连接期间不可更改（需重连才能切换语言）。

#### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `lang` | string | 指定 ASR 识别语言，不传则服务端默认偏中文识别 |

#### 支持的语言值

| 显示名称 | URL 参数 | 说明 |
|----------|----------|------|
| 默认 | （不传 `lang`） | 中英混合，偏中文 |
| 中文 | `lang=zh` | 中英混合，偏中文 |
| 英语 | `lang=en` | 中英混合，偏英文 |
| 广东话 | `lang=zh_yue` | 粤语方言 |
| 四川话 | `lang=zh_sc` | 四川方言 |
| 苏州话 | `lang=zh_su` | 苏州方言 |
| 日语 | `lang=ja` | |
| 西班牙语 | `lang=es` | |
| 俄语 | `lang=ru` | |
| 韩语 | `lang=ko` | |
| 越南语 | `lang=vi` | |
| 德语 | `lang=de` | |
| 阿拉伯语 | `lang=ar` | |
| 印尼语 | `lang=id` | |
| 泰语 | `lang=th` | |
| 马来语 | `lang=ms` | |
| 葡萄牙语 | `lang=pt` | |
| 乌兹别克语 | `lang=uz` | |
| 波兰语 | `lang=pl` | |
| 波斯语 | `lang=fa` | |

#### 连接 URL 示例

不传语言参数（默认中英混合）：
```
wss://<host>/ws/chatbot/?token=<access>&nonce=<nonce_ws>&sign=<sign_ws>
```

指定中文（`lang=zh`）：
```
wss://<host>/ws/chatbot/?token=<access>&nonce=<nonce_ws>&sign=<sign_ws>&lang=zh
```

指定日语（`lang=ja`）：
```
wss://<host>/ws/chatbot/?token=<access>&nonce=<nonce_ws>&sign=<sign_ws>&lang=ja
```

#### 代码示例（Python）

```python
from urllib.parse import urlencode

# 基础参数
params = {
    "token": access_token,
    "nonce": nonce_ws,
    "sign": sign_ws,
}

# lang 示例值：
#   ""       -> 不传 lang（默认，中英混合偏中文）
#   "zh"     -> 中文
#   "en"     -> 英语（中英混合偏英文）
#   "ja"     -> 日语
#   "zh_yue" -> 广东话
lang = "zh"  # 按需修改

if lang:
    params["lang"] = lang

ws_url = f"wss://<host>/ws/chatbot/?{urlencode(params)}"
```

> **注意**：语言参数在认证（获取 `nonce_ws/sign_ws`）之后、建立 WebSocket 连接之前拼入 URL。切换语言时需重新走一次认证流程并重建连接。

### 3.2 关闭码（Close Code）

服务端会在握手后主动关闭（客户端应根据 code 做重试或提示）：

- `4001`：未授权（token 无效 / nonce 不存在或过期 / sign 校验失败 / 设备不存在或被禁用）
- `4002`：当日使用时长超限（见 6. 用量限制）

## 4. 消息协议（客户端与服务端之间）

该 WS 同时使用两种 frame：

- Binary frame：原始音频字节流
- Text frame：JSON 控制/文本消息

### 4.1 上行（客户端 -> 服务端）

1) 语音输入（binary）

- 客户端在“按住说话”期间，持续发送 binary frame。
- binary 内容为原始 PCM 音频字节（服务端声明为 `pcm16` 输入）。
- 建议：小块发送（例如 20ms 到 100ms 一帧），避免单帧过大造成延迟抖动。

2) 松开按键/停止说话（text）

当用户结束一轮说话（例如松开按钮）后，发送：
```json
{"action":"stop_speaking"}
```

服务端会提交输入缓冲并触发一次回答生成。

3) 打断当前回答（text）

当用户需要打断正在播报的回答并立即开始新一轮说话时，发送：
```json
{"action":"interrupt"}
```

服务端会取消当前回答并清空输入缓冲，随后你可以继续发送新的音频 binary frame。

### 4.2 下行（服务端 -> 客户端）

1) TTS 音频输出（binary）

- 服务端会以 binary frame 方式持续下发回答音频 chunk，客户端应边收边播放。
- 服务端当前配置的输出音频格式为 `pcm24`（24-bit PCM 原始字节流）。

2) 文本转写增量（text）

服务端会下发 text frame（JSON）表示增量转写：
```json
{"action":"transcript","text":"..."}
```

说明：

- `text` 为增量片段（delta），客户端可将其追加到当前显示文本上。

## 5. 推荐的客户端状态机

1. 连接前：确保已有 `access token`，并获取 `nonce_ws/sign_ws`。
2. 建立 WS：连接成功后进入 `IDLE`。
3. `IDLE -> RECORDING`：用户按住说话，开始周期性发送 PCM16 binary 帧。
4. `RECORDING -> WAITING`：用户松开按钮，发送 `{"action":"stop_speaking"}`，停止上行音频。
5. `WAITING -> PLAYING`：开始接收回答音频 binary 并播放，同时接收转写 text 并显示。
6. `PLAYING -> RECORDING`：若用户打断，先发送 `{"action":"interrupt"}`，停止播放，立刻进入录音并发送新音频。
7. 任意状态断线：若 close code 为 `4001/4002` 按原因处理；否则重新获取 `nonce_ws/sign_ws` 后重连。

## 6. 用量限制与连接管理

服务端会按“连接持续时间”累计当日使用时长（不是纯说话时长）：

- 当日上限：`5 小时`（`5 * 60 * 60` 秒）
- 超限后将拒绝新连接（close code `4002`）

建议：

- 不用时及时断开 WS，避免空闲连接持续计费。
- 断线重连前重新获取 `nonce_ws/sign_ws`，不要复用旧 nonce。

## 7. 示例代码（Python，演示握手与 WS 交互骨架）

下面示例只演示流程与消息格式；音频采集与播放请按你的平台实现。

```python
import requests, hmac, hashlib, json, asyncio, websockets

HOST = ""
BASE_HTTP = f"https://{HOST}"
BASE_WS = f"wss://{HOST}"

DEVICE_ID = "LYY-202603-000123"
DEVICE_SECRET = "<device_secret>"

def hmac_hex(secret: str, nonce: str) -> str:
    return hmac.new(secret.encode("utf-8"), nonce.encode("utf-8"), hashlib.sha256).hexdigest()

def get_nonce() -> str:
    r = requests.post(f"{BASE_HTTP}/device/challenge/", json={"device_id": DEVICE_ID}, timeout=10)
    r.raise_for_status()
    return r.json()["nonce"]

def get_tokens():
    nonce = get_nonce()
    sig = hmac_hex(DEVICE_SECRET, nonce)
    r = requests.post(f"{BASE_HTTP}/device/token/", json={"device_id": DEVICE_ID, "signature": sig}, timeout=10)
    r.raise_for_status()
    return r.json()["access"], r.json()["refresh"]

async def main():
    access, _refresh = get_tokens()

    # 每次 WS 连接前单独取一次 nonce/sign
    nonce_ws = get_nonce()
    sign_ws = hmac_hex(DEVICE_SECRET, nonce_ws)

    # 语言参数（可选）：
    #   ""       -> 不传 lang，服务端默认中英混合偏中文
    #   "zh"     -> 中文
    #   "en"     -> 英语（中英混合偏英文）
    #   "ja" / "ko" / ... -> 其他语言，见文档 3.2 节
    lang = ""  # 按需修改

    from urllib.parse import urlencode
    params = {"token": access, "nonce": nonce_ws, "sign": sign_ws}
    if lang:
        params["lang"] = lang
    ws_url = f"{BASE_WS}/ws/chatbot/?{urlencode(params)}"
    async with websockets.connect(ws_url, ping_interval=None) as ws:
        # 1) 发送若干音频块（二进制）。此处用假数据占位。
        # pcm16_bytes = capture_pcm16_chunk()
        # await ws.send(pcm16_bytes)

        # 2) 停止说话，触发回答
        await ws.send(json.dumps({"action": "stop_speaking"}))

        # 3) 接收：binary 为音频，text 为 transcript
        while True:
            msg = await ws.recv()
            if isinstance(msg, bytes):
                # play_pcm24(msg)
                pass
            else:
                data = json.loads(msg)
                if data.get("action") == "transcript":
                    print(data.get("text", ""), end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
```

## 8. 常见问题与排查

- 连接后立即被断开且 code=4001：
  - 检查 `token/nonce/sign` 三者是否都带上了。
  - 确认 `nonce_ws` 是刚从 `/device/challenge/` 获取且未过期（60s）且未被复用。
  - 确认 `sign_ws` 算法是 `HMAC_SHA256(device_secret, nonce_ws)`，输出 hex。
- 返回 `challenge expired or not found`：
  - nonce 过期或已被消费，重新调用 `/device/challenge/`。
- 无法播放音频：
  - 服务端下发为原始 `pcm24`，客户端需按 24-bit PCM 解码/播放（采样率、声道需与你的设备约定一致）。
