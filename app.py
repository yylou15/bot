import json
import _thread
from flask import Flask, request

from api.api import send_message
from api.handler import text_analysis
from api.token import gen_tenant_token
from util.AESCipher import AESCipher

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback', methods=['POST'])
def call_back():
    call_back_data = (AESCipher("eh5NGHN8izW5HzkrZSaN5fmhdqvUIPmK").decrypt_string(request.get_json()['encrypt']))
    good, msg = text_analysis(call_back_data['event']['text_without_at_bot'])
    if not good:
        reply_id = call_back_data['event']['open_message_id']
        send_message(call_back_data['event']['open_chat_id'], "消息审核未通过，{}".format(msg), reply_id)
    return call_back_data


if __name__ == '__main__':
    _thread.start_new_thread(gen_tenant_token, ("Thread-1", 2,))
    app.run()
