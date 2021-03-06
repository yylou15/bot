import json
import _thread
from flask import Flask, request

from api.api import send_message
from api.baidu.text import text_analysis, text_correct
from api.token import gen_tenant_token
from util.AESCipher import AESCipher

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback', methods=['POST'])
def call_back():
    call_back_data = json.loads(
        AESCipher("eh5NGHN8izW5HzkrZSaN5fmhdqvUIPmK").decrypt_string(request.get_json()['encrypt']))
    # good, msg = text_analysis(call_back_data['event']['text_without_at_bot'])
    wrongs = text_correct(call_back_data['event']['text_without_at_bot'])
    if wrongs:
        reply_id = call_back_data['event']['open_message_id']
        txt = ""
        for wrong in wrongs:
            txt += "{}->{}.".format(wrong, wrongs[wrong])
        send_message(call_back_data['event']['open_chat_id'], txt, reply_id)
    print(call_back_data)

    return call_back_data


if __name__ == '__main__':
    _thread.start_new_thread(gen_tenant_token, ())
    app.run()
