import time
import json
import hashlib
import requests
from urllib.request import urlopen
from urllib.parse import urlencode

"""可更改的参数"""
webhook = '网址'
reminders = ['手机号',]
user_txt = '账号'
passwd_txt = '账号密码'
url_txt = "接口地址"

"""企业宝"""
timedoc = time.time()
timedoc1000 = str((int(round(timedoc * 1000))))
passwdtime = (passwd_txt + timedoc1000)
passtime = passwdtime.encode("utf-8")
passmd5 = hashlib.md5()
passmd5.update(passtime)
passwdmd5 = passmd5.hexdigest()
par = {'account' : user_txt, 'signature' : passwdmd5 , 'timestamp' :timedoc1000 }
par_txt = urlencode(par)
res = urlopen(url_txt,par_txt.encode())
resline = (res.readline().decode())
reslineget = eval(resline).get("data").get("balance")
res_txt = str(reslineget)
msg = "你好，你的短信为 " + res_txt

"""钉钉机器人快捷发信息"""
def send_msg(webhook, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(webhook, data=json.dumps(data), headers=headers)
    return r.text

"""执行程序"""
send_msg(webhook, reminders, msg)
