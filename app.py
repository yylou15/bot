import json
import requests

from flask import Flask, request

from common.headers import send_headers
from util.AESCipher import AESCipher

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback', methods=['POST'])
def decrypt():
    data = json.loads(AESCipher("eh5NGHN8izW5HzkrZSaN5fmhdqvUIPmK").decrypt_string(request.get_json()['encrypt']))
    print(data)
    if data['event']['text_without_at_bot'].strip() == '整点笑话':
        xiaohua = json.loads(requests.post("http://api.apishop.net/common/joke/getJokesByRandom", data={
            "apiKey": "5ZULlnD5f01345b094672e3ea5b6f7e1d299e1777930ac3",
            "pageSize": "1"
        }).text)['result'][0]['content']

        chat_id = data['event']['open_chat_id']
        print(requests.post("https://open.feishu.cn/open-apis/message/v4/send/", headers=send_headers, data=json.dumps({
            "chat_id": chat_id,
            "msg_type": "text",
            "content": {
                "text": xiaohua
            }
        })).text)
        return "?"
    return data


if __name__ == '__main__':
    app.run()
