import json
import time
import requests

def checkinapi():
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
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": ''
        }
        return requests.post(checkin_url, data={},headers=headers)

def checkin():
    try:
        r = checkinapi()
        # print(r.text)
    except:
        print('签到接口请求失败！')
        exit(1)
    if r.status_code == 200:
        info = json.loads(r.text)
        total = info['total'] / 1048576
        space = info['space'] / 1048576
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info['time'] / 1000))
        is_success = info['success']
        
        if is_success == 1:
            print('签到成功，本次签到获得：{} M | 总共获得：{} M | 签到时间：{}'.format(space, total, t))
        elif is_success == 0:
            print('今日已签到 | 签到时间：{} | 总共获得：{} M '.format(t, total))
    else:
        print(f'请求失败，状态码：{r.status_code}')
        exit(1)

if __name__ == "__main__":
    checkin()