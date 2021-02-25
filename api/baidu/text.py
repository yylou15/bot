import json

import requests

from aip import AipContentCensor

""" 你的 APPID AK SK """
APP_ID = '23632338'
API_KEY = 'iOdlKgcSfjsMqIr5T2aSe6Zn'
SECRET_KEY = 'PwX7drvhQfKQ2LiNmuVsGohrzZnquyUG'

client = AipContentCensor(APP_ID, API_KEY, SECRET_KEY)


def text_analysis(text: str) -> (bool, str):
    res = (client.textCensorUserDefined(text))
    if res['conclusion'] == "合规":
        return True, ""

    msg = ""
    for item in res['data']:
        msg += item['msg'] + "."
    return False, msg


def text_correct(text: str) -> ({}):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(API_KEY,SECRET_KEY)
    token = requests.get(host).json()['access_token']
    res = requests.post("https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet?access_token={}".format(token),data=json.dumps({
        "百度是一家人工只能公司"
    }))
    print(res)