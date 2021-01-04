import json
import requests

from flask import Flask, request

from common.headers import send_headers
from util.AESCipher import AESCipher

app = Flask(__name__)

session = requests.Session()
session.headers = send_headers


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback', methods=['POST'])
def call_back():
    data = json.loads(AESCipher("eh5NGHN8izW5HzkrZSaN5fmhdqvUIPmK").decrypt_string(request.get_json()['encrypt']))
    print(data)
    if '笑话' in data['event']['text_without_at_bot'].strip():
        xiaohua = json.loads(requests.post("http://api.apishop.net/common/joke/getJokesByRandom", data={
            "apiKey": "5ZULlnD5f01345b094672e3ea5b6f7e1d299e1777930ac3",
            "pageSize": "1"
        }).text)['result'][0]['content']

        chat_id = data['event']['open_chat_id']
        res = json.loads(session.post("https://open.feishu.cn/open-apis/message/v4/send/", data=json.dumps({
            "chat_id": chat_id,
            "msg_type": "text",
            "content": {
                "text": xiaohua
            }
        })).text)
        print(res['code'])
        print(res['code'] == 99991663)
        if res['code'] == 99991663:
            token_res = json.loads(session.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/", data={
                "app_id": "cli_9f67c7eaccb0500b",
                "app_secret": "opy4NazX54hx8W0CRj4cqdK1eF0oQBGw"
            }).text)
            print(token_res)
            send_headers['Authorization'] = "Bearer {}".format(token_res['tenant_access_token'])
            call_back()

    # else:
    #     chat_id = data['event']['open_chat_id']
    #     print(requests.post("https://open.feishu.cn/open-apis/message/v4/send/", headers=send_headers, data=json.dumps({
    #         "chat_id": chat_id,
    #         "msg_type": "text",
    #         "content": {
    #             "text": "你问我？"
    #         }
    #     })).text)
    return data


if __name__ == '__main__':
    app.run()
