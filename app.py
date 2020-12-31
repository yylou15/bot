import json

from flask import Flask, request

from util.AESCipher import AESCipher

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback', methods=['POST'])
def decrypt():
    challenge = json.loads(AESCipher("eh5NGHN8izW5HzkrZSaN5fmhdqvUIPmK").decrypt_string(request.get_json()['encrypt']))['challenge']
    print(challenge)
    return challenge


if __name__ == '__main__':
    app.run()
