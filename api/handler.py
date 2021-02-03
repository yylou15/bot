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
