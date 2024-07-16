import requests
import json


class YoudaoNoteApi(object):
    """
    有道云笔记 API 封装
    原理：https://depp.wang/2020/06/11/how-to-find-the-api-of-a-website-eg-note-youdao-com/
    """
    # 获取根目录id
    ROOT_ID_URL = 'https://note.youdao.com/yws/api/personal/file?method=getByPath&keyfrom=web&cstk={cstk}'
    # 获取指定目录ID的基本信息，以及该目录下的文件和目录
    DIR_MES_URL = 'https://note.youdao.com/yws/api/personal/file/{dir_id}?all=true&f=true&len=1000&sort=1' \
                  '&isReverse=false&method=listPageByParentId&keyfrom=web&cstk={cstk}'
    FILE_URL = 'https://note.youdao.com/yws/api/personal/sync?method=download&_system=macos&_systemVersion=&' \
               '_screenWidth=1280&_screenHeight=800&_appName=ynote&_appuser=0123456789abcdeffedcba9876543210&' \
               '_vendor=official-website&_launch=16&_firstTime=&_deviceId=0123456789abcdef&_platform=web&' \
               '_cityCode=110000&_cityName=&sev=j1&keyfrom=web&cstk={cstk}'

    def __init__(self, cookies_path=None):
        """
        初始化
        :param cookies_path:
        """
        self.session = requests.session()  # 使用 session 维持有道云笔记的登陆状态
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/100.0.4896.88 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.cookies_path = cookies_path if cookies_path else 'cookies.json'
        self.cstk = None

    def login_by_cookies(self) -> str:
        """
        使用 Cookies 登录，其实就是设置 Session 的 Cookies
        :return: error_msg
        """
        try:
            cookies = self._covert_cookies()
        except Exception as err:
            return format(err)
        for cookie in cookies:
            self.session.cookies.set(name=cookie[0], value=cookie[1], domain=cookie[2], path=cookie[3])
        self.cstk = cookies[0][1] if cookies[0][0] == 'YNOTE_CSTK' else None  # cstk 用于请求时接口验证
        if not self.cstk:
            return 'YNOTE_CSTK 字段为空'
        print('本次使用 Cookies 登录')

    def _covert_cookies(self) -> list:
        """
        读取 cookies 文件的 cookies，并转换为字典
        :return: cookies
        """
        with open(self.cookies_path, 'rb') as f:
            json_str = f.read().decode('utf-8')

        try:
            cookies_dict = json.loads(json_str)  # 将字符串转换为字典
            cookies = cookies_dict['cookies']
        except Exception:
            raise Exception('转换「{}」为字典时出现错误'.format(self.cookies_path))
        return cookies

    def http_post(self, url, data=None, files=None):
        """
        封装 post 请求
        :param url:
        :param data:
        :param files:
        :return: response
        """
        return self.session.post(url, data=data, files=files)

    def http_get(self, url):
        """
        封装 get 请求
        :param url:
        :return: response
        """
        return self.session.get(url)

    def get_root_dir_info_id(self) -> dict:
        """
        获取有道云笔记根目录信息
        :return: {
            'fileEntry': {'id': 'test_root_id', 'name': 'ROOT', ...},
            ...
        }
        """
        data = {'path': '/', 'entire': 'true', 'purge': 'false', 'cstk': self.cstk}
        return self.http_post(self.ROOT_ID_URL.format(cstk=self.cstk), data=data).json()

    def get_dir_info_by_id(self, dir_id) -> dict:
        """
        根据目录 ID 获取目录下所有文件信息
        :return: {
            'count': 3,
            'entries': [
                 {'fileEntry': {'id': 'test_dir_id', 'name': 'test_dir', 'dir': true, ...}},
                 {'fileEntry': {'id': 'test_note_id', 'name': 'test_note', 'dir': false, ...}}
                 ...
            ]
        }
        """
        url = self.DIR_MES_URL.format(dir_id=dir_id, cstk=self.cstk)
        res = self.http_get(url)
        if res.status_code >= 500:
            return self.http_get(url).json()
        return res.json()

    def get_file_by_id(self, file_id):
        """
        根据文件 ID 获取文件内容
        :param file_id:
        :return: response，内容为笔记字节码
        """
        data = {'fileId': file_id, 'version': -1, 'convert': 'true', 'editorType': 1, 'cstk': self.cstk}
        url = self.FILE_URL.format(cstk=self.cstk)
        return self.http_post(url, data=data)
    
    def checkin(self):
        """ 签到领空间
        return: {
            "multiple": 1,
            "originSpace": 2097152,
            "total": 424673280,
            "time": 1692543594831,
            "success": 1,
            "space": 2097152
        }  
        """
        checkin_url = 'https://note.youdao.com/yws/mapi/user?method=checkin'
        return self.http_post(checkin_url,data={})
    
    def note_rename(self,note_name,file_id):
        url = f'https://note.youdao.com/yws/api/personal/sync?method=push&name={note_name}fileId={file_id}&domain=0&rootVersion=-1&sessionId=&modifyTime=1692786849&transactionId={file_id}&transactionTime=1692786849&editorVersion=1692267502000&tags=&_system=windows&_systemVersion=&_screenWidth=1920&_screenHeight=1080&_appName=ynote&_appuser=019623eb3bfaff1f5ddc278090f8420d&_vendor=official-website&_launch=22279&_firstTime=2023/08/19 11:24:10&_deviceId=8cf8855c4105f937&_platform=web&_cityCode=440300&_cityName=深圳&sev=j1&sec=v1&keyfrom=web&cstk={self.cstk}'