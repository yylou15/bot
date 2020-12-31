import json

import requests

from common.headers import send_headers

# print(requests.post("https://open.feishu.cn/open-apis/message/v4/send/", headers=send_headers, data=json.dumps({
#     "chat_id": "oc_9f176f68b3a8435583dc6ec8d0abe513",
#     "msg_type": "text",
#     "content": {
#         "text": "text content"
#     }
# })).text)

print(json.loads(requests.post("http://api.apishop.net/common/joke/getJokesByRandom", data={
            "apiKey": "5ZULlnD5f01345b094672e3ea5b6f7e1d299e1777930ac3",
            "pageSize": "1"
        }).text)['result'][0]['content'])