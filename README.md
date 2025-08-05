[toc]

# youdaonote-pull

此脚本可将有道云的所有的笔记下载到本地，可以作为有道云笔记的迁移或者本地备份。脚本参考了 [youdaonote-pull](https://github.com/DeppWang/youdaonote-pull.git)，在其基础上添加了json格式的转换。目前新建有道云笔记爬取下来的格式为JSON，以前的是xml格式。脚本转换了一些常用的格式，例如，标题、加粗、表格、图片、文件、列表、下划线、颜色等，有些格式和属性可能没有考虑到，笔记可能有些缺失，下载下来后，请检查一下。

## 功能

### 常用功能

- 可将所有笔记（文件）按原格式下载到本地
- 有道云的正常笔记爬取后是 `xml`和 `json`格式，不是正常笔记内容，需要**将其转换为 `Markdown`格式**
- 由于有道云笔记图床图片不能在有道云笔记外显示，**默认将其下载到本地，或指定上传到 [SM.MS](https://sm.ms)**

### 功能优化

图片名字方案

* 使用文件名+\_image_index.png作为图片的文件名。优点就是很容易知道图片是哪个笔记的，缺点就是有道云上的笔记改名字后，重新下载下来，旧笔记的图片还会存在，占用空间，需要手动清理，笔记麻烦
* 通过图片内容生成md5，使用md5作为图片的文件名。优点是笔记改名后，图片内容不变，文件名也不会变，那就无须重新写入；缺点就是图片不好找，不过一般情况是在笔记中看图片，也不会找实际的图片，这个影响好像也不大。

## 使用步骤

### 导出前的准备工作

#### 1、安装  [Git](https://git-scm.com/downloads)、clone 项目

- 可根据 [廖雪峰 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496) 安装 Git，测试是否安装成功

```sh
git --version
```

- 打开命令行软件，如 Terminal (macOS)、PowerShell (Windows)，clone 项目，里面包含脚本

```shell
git clone https://github.com/chunxingque/youdaonote-pull.git
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

# 虚拟环境
python3 -m venv app-venv
```

```shell
# Windows
pip install -r requirements.txt

# 有问题可参考 https://www.liaoxuefeng.com/wiki/1016959663602400/1017493741106496

# 虚拟环境
app-venv/bin/pip install -r requirements.txt
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

**Cookie获取js脚本**

用上面的方式寻找Cookie让人眼瞎
因此编写此脚本
使用方式：
浏览器F12打开开发者工具，找到控制台把脚本粘贴进去，替换tmp_cookie的值
回车，即可得到一份身份认证Cookie配置文件
（YNOTE_SESS属性有HttpOnly属性，不然这个脚本可以更简单）

```javascript
var tmp_cookie = '这里把上图Cookie属性的值丢进来'

function getCookies() {
    var cookies = tmp_cookie.split(';');
    var result = [];
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        var parts = cookie.split('=');
        var name = parts[0];
        var value = parts[1];
        if (name === 'YNOTE_CSTK' || name === 'YNOTE_LOGIN' || name === 'YNOTE_SESS') {
            result.push([name, value, '.note.youdao.com', '/']);
        }
    }
    return result;
}

function formatCookies(cookies) {
    return {
        cookies: cookies
    };
}

var cookies = getCookies();
var formattedCookies = formatCookies(cookies);
// 网站屏蔽了日志或者设置了console的日志级别，因此这里使用warn级别，可以正常打印
console.warn(JSON.stringify(formattedCookies, null, 2))
```

- 提示：脚本单纯本地运行，不用担心你的 `Cookies` 泄露

#### 4、设置脚本参数配置文件 `config.json`

建议使用 [Sublime](https://www.sublimetext.com/3) 等三方编辑器编辑 `config.json`，避免编码格式错误

```json
{
    "local_dir": "",
    "ydnote_dir": "",
    "smms_secret_token": "",
    "is_relative_path": true,
    "del_spare_file": false,
    "del_spare_dir": false
}
```

* `local_dir`：选填，本地存放导出文件的文件夹，不填则默认为当前文件夹
* `ydnote_dir`：选填，有道云笔记目录，默认会下载该所有的笔记，支持多层目录，例如：根目录/子目录/子子目录
* `smms_secret_token`：选填， [SM.MS](https://sm.ms) 的 `Secret Token`（注册后 -> Dashboard -> API Token），用于上传笔记中有道云图床图片到 SM.MS 图床，不填则只下载到本地（`youdaonote-images` 文件夹），`Markdown` 中使用本地链接
* `is_relative_path`：在 MD 文件中图片 / 附件是否采用相对路径展示，默认true
* del_spare_file: 删除本地多余的文件，如果有道笔记上没有的文件，将会被删除
* del_spare_dir：删除本地多余的目录，如果有道笔记上没有的目录，将会被删除

注意：del_spare_file和del_spare_dir这两个参数是为了方便清理本地多余的文件或目录，这些文件或者目录是在有道云上被删除或者重命名的，如果手动清理比较麻烦。建议自动清理多余的文件，然后手动清理多余的目录。


### 运行导出脚本

```shell
python3 pull_notes.py  # macOS/Linux
python  pull_notes.py  # Windows
app-venv/bin/python pull_notes.py # 虚拟环境
```

如果某个笔记拉取失败，可能是笔记格式比较旧，可以新建一个新笔记，把旧笔记内容复制到新笔记，重新拉取，基本都可以解决。

建议笔记名称不要使用特殊符号，例如：#、/、:、空格、英文括号等，可以使用_和-符号替代，不然容易报错

### 多次导出

多次导出时，同样使用以下命令：

```shell
python3 pull_notes.py  # macOS/Linux
python  pull_notes.py   # Windows
```

根据有道云笔记文件最后修改时间是否大于本地文件最后修改时间来判断是否需要更新。再次导出时，只会导出有道云笔记上次导出后新增、修改或未导出的笔记，不会覆盖本地已经修改的文件。**但有道云笔记和本地不要同时修改同一个文件，这样可能会导致本地修改丢失**！

更新时，会重新下载文件并覆盖原文件，图片也会重新下载。

## 代码调试

### JSON格式转换调试

目前有道云新版的笔记采用JSON格式，转换JSON格式出现问题时，需要提供详细内容和截图等，有能力的，登录有道云的web端，获取有问题笔记的JSON文件，提供给我，方便我代码调试。

有道云JSON格式： `test/test.json`

转换好的md文件：`test/test.md`

格式转换测试

```
python3 core/convert.py
```

json数据格式说明

* 键3是一个文本的标识id
* 键4是一个字典，里面存储着键值对，是不同类型文本的属性值，列如，标题类型，就有h1,h2,h3等属性
* 键5是一个列表，存储着字典
* 键6标识文本的类型，列如：标题，表格和链接等
* 键7是一个列表，存储着字典，一个键7列表表示一行文本
* 键8是一串字符串，存储着原始文本
* 键9是一个列表，存储着字典，字典中的键2表示文本的属性(加粗，斜体和颜色等)，键0表示颜色

### 有道云接口说明

获取笔记接口：`https://note.youdao.com/yws/api/personal/sync`

## 注意事项

1. 如果你自己修改脚本，注意不要将 `cookies.json` 文件 `push` 到 GitHub
2. 如果你不是开发者，可能对上面的命令行操作有所陌生，建议按步骤慢慢操作一遍
3. 请确认代码是否为最新，有问题请先看 [issue](https://github.com/chunxingque/youdaonote-pull/issues) 是否存在，不存在再提 issue

正常用户浏览器操作时，浏览器（前端）调用服务器（后端）接口，接口返回文件内容由前端渲染显示。原理是[找到有道云笔记的接口](https://depp.wang/2020/06/11/how-to-find-the-api-of-a-website-eg-note-youdao-com)，模拟操作接口，将前端显示改为存放到本地。Xml 转换为 Markdown，借助了 [xml.etree.ElementTreeI](http://docs.python.org/3.7/library/xml.etree.elementtree.html)

## 感谢（参考）

- [YoudaoNoteExport](https://github.com/wesley2012/YoudaoNoteExport)
- [youdaonote-pull](https://github.com/DeppWang/youdaonote-pull.git)
