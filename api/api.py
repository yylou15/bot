import json

from api import oapi_session


def get_group_members(chat_id) -> []:
    return json.loads(
        oapi_session.post("https://open.feishu.cn/open-apis/chat/v4/members?chat_id={}".format(chat_id)).text)


def send_message(chat_id: str, text: str, reply_id: str):
    print(oapi_session.post("https://open.feishu.cn/open-apis/message/v4/send/", data=json.dumps({
        "chat_id": chat_id,
        "msg_type": "text",
        "root_id": reply_id,
        "content": {
            "text": text
        }
    })).text)
