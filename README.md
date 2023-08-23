# youdaonote-pull

此脚本可将有道云的所有的笔记下载到本地。代码参考了 [youdaonote-pull](https://github.com/DeppWang/youdaonote-pull.git)，目前新建有道云笔记爬取下来的格式为JSON，以前的是xml格式，而[youdaonote-pull](https://github.com/DeppWang/youdaonote-pull.git) 目前不支持JSON格式的转换，因此此脚本添加json格式的转换。脚本转换了一些常用的格式，例如，标题、加粗、表格、图片、文件、列表等，有些格式和属性可能没有考虑到，笔记可能有些缺失，下载下来后，请检查一下。

## 功能

- 可将所有笔记（文件）按原格式下载到本地
- 有道云的正常笔记爬取后是 `xml`和 `json`格式，不是正常笔记内容，需要**将其转换为 `Markdown`格式**
- 由于有道云笔记图床图片不能在有道云笔记外显示，**默认将其下载到本地，或指定上传到 [SM.MS](https://sm.ms)**

## 使用步骤

### 一、导出前的准备工作

#### 1、安装  [Git](https://git-scm.com/downloads)、clone 项目

- 可根据 [廖雪峰 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496) 安装 Git，测试是否安装成功

```sh
git --version
```

- 打开命令行软件，如 Terminal (macOS)、PowerShell (Windows)，clone 项目，里面包含脚本

```shell
pwd
git clone https://github.com/DeppWang/youdaonote-pull.git
cd youdaonote-pull
```

#### 2、安装 [Python3](https://www.python.org/downloads/)、安装依赖模块（包）

- 可根据 [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624) 安装 Python3，测试是否安装成功

```shell
python3 --version  # macOS/Linux
python --version   # Windows
```

- 安装依赖包

```shell
# macOS
sudo easy_install pip3      # 安装 Python3 Package Installer
sudo pip3 install -r requirements.txt
```

```shell
# Windows
pip install -r requirements.txt

# 有问题可参考 https://www.liaoxuefeng.com/wiki/1016959663602400/1017493741106496
```

#### 3、设置登录 `Cookies` 文件 `cookies.json`

```json
{
    "cookies": [
        [
            "YNOTE_CSTK",
            "**",
            ".note.youdao.com",
            "/"
        ],
        [
            "YNOTE_LOGIN",
            "**",
            ".note.youdao.com",
            "/"
        ],
        [
            "YNOTE_SESS",
            "**",
            ".note.youdao.com",
            "/"
        ]
    ]
}
```

由于有道云笔记登录升级，**目前脚本不能使用账号密码登录，只能使用 `Cookies` 登录。**

获取 `Cookies` 方式：

1. 在浏览器如 Chrome 中使用账号密码或者其他方式登录有道云笔记
2. 打开 DevTools (F12)，Network 下找「主」请求（一般是第一个），再找 `Cookie`
3. 复制对应数据替换  `**`

![image.png](https://s2.loli.net/2022/04/04/N47KPEaSGvCpsfX.png)

示例：

```json
{
    "cookies": [
        [
            "YNOTE_CSTK",
            "rR_Pejz0",
            ".note.youdao.com",
            "/"
        ],
        [
            "YNOTE_LOGIN",
            "3||1649054441155",
            ".note.youdao.com",
            "/"
        ],
        [
            "YNOTE_SESS",
            "v2|BdllbnwfaWl5RMUWOfqZ0gShf***6LqFRqB0MYfh4JLR",
            ".note.youdao.com",
            "/"
        ]
    ]
}
```

- 提示：脚本单纯本地运行，不用担心你的 `Cookies` 泄露

#### 4、设置脚本参数配置文件 `config.json`

建议使用 [Sublime](https://www.sublimetext.com/3) 等三方编辑器编辑 `config.json`，避免编码格式错误

```json
{
    "local_dir": "",
    "ydnote_dir": "",
    "smms_secret_token": "",
    "is_relative_path": true
}
```

* `local_dir`：选填，本地存放导出文件的文件夹，不填则默认为当前文件夹
* `ydnote_dir`：选填，有道云笔记指定导出文件夹名，不填则导出所有文件，只支持有道云笔记根目录的文件夹，不支持直接导出子目录的笔记
* `smms_secret_token`：选填， [SM.MS](https://sm.ms) 的 `Secret Token`（注册后 -> Dashboard -> API Token），用于上传笔记中有道云图床图片到 SM.MS 图床，不填则只下载到本地（`youdaonote-images` 文件夹），`Markdown` 中使用本地链接
* `is_relative_path`：选填，在 MD 文件中图片 / 附件是否采用相对路径展示，不填或 false 为绝对路径，true 为相对路径

示例：

- macOS

```json
{
    "local_dir": "/Users/deppwang/Documents/youdaonote-pull/test",
    "ydnote_dir": "",
    "smms_secret_token": "SGSLk9yWdTe4RenXYqEPWkqVrx0Yexample"
}
```

- Windows

```json
{
    "local_dir": "D:/Documents/youdaonote-pull/test",
    "ydnote_dir": "",
    "smms_secret_token": "SGSLk9yWdTe4RenXYqEPWkqVrx0Yexample"
}
```

### 二、运行导出脚本

```shell
python3 pull_notes.py  # macOS/Linux
python  pull_notes.py  # Windows
```

如果某个笔记拉取失败，可能是笔记格式比较旧，可以新建一个新笔记，把旧笔记内容复制到新笔记，重新拉取，基本都可以解决。

建议笔记名称不要使用特殊符号，例如：#、/、:、空格、英文括号等，可以使用_和-符号替代，不然容易报错


### 三、多次导出

多次导出时，同样使用以下命令：

```shell
python3 pull_notes.py  # macOS/Linux
python  pull_notes.py   # Windows
```

根据有道云笔记文件最后修改时间是否大于本地文件最后修改时间来判断是否需要更新。再次导出时，只会导出有道云笔记上次导出后新增、修改或未导出的笔记，不会覆盖本地已经修改的文件。**但有道云笔记和本地不要同时修改同一个文件，这样可能会导致本地修改丢失**！

更新时，会重新下载文件并覆盖原文件，图片也会重新下载。

## 注意事项

1. 如果你自己修改脚本，注意不要将 `cookies.json` 文件 `push` 到 GitHub
2. 如果你不是开发者，可能对上面的命令行操作有所陌生，建议按步骤慢慢操作一遍
3. 请确认代码是否为最新，有问题请先看 [issue](https://github.com/chunxingque/youdaonote-pull/issues) 是否存在，不存在再提 issue
   ```bash
   git pull origin master  # 更新代码
   ```

正常用户浏览器操作时，浏览器（前端）调用服务器（后端）接口，接口返回文件内容由前端渲染显示。原理是[找到有道云笔记的接口](https://depp.wang/2020/06/11/how-to-find-the-api-of-a-website-eg-note-youdao-com)，模拟操作接口，将前端显示改为存放到本地。Xml 转换为 Markdown，借助了 [xml.etree.ElementTreeI](http://docs.python.org/3.7/library/xml.etree.elementtree.html)

## 感谢（参考）

- [YoudaoNoteExport](https://github.com/wesley2012/YoudaoNoteExport)
- [youdaonote-pull](https://github.com/DeppWang/youdaonote-pull.git)
