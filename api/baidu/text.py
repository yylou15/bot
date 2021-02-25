import json

import requests

from aip import AipContentCensor, AipNlp

""" 你的 APPID AK SK """
APP_ID = '23632338'
API_KEY = 'iOdlKgcSfjsMqIr5T2aSe6Zn'
SECRET_KEY = 'PwX7drvhQfKQ2LiNmuVsGohrzZnquyUG'

client = AipContentCensor(APP_ID, API_KEY, SECRET_KEY)
textClient = AipNlp("18093160", "PF6eGkEh1Wn65qo6fzYwvfWZ", "VlQvfsGp2yImtbEGdTRGxB8NHzNkPPQe")


def text_analysis(text: str) -> (bool, str):
    res = (client.textCensorUserDefined(text))
    if res['conclusion'] == "合规":
        return True, ""

    msg = ""
    for item in res['data']:
        msg += item['msg'] + "."
    return False, msg


def text_correct(text: str) -> ({}):
    res = textClient.ecnet(text)
    ret = {}
    if res and res['item']:
        for wrongs in res['item']['vec_fragment']:
            ret[wrongs["ori_frag"]] = wrongs['correct_frag']
    return ret
