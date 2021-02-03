import _thread
import time

from api import oapi_session
from api.api import get_group_members, send_message
from api.token import gen_tenant_token, gen_user_token, gen_app_token, gen_auth_code_url

# print(requests.post("https://open.feishu.cn/open-apis/message/v4/send/", headers=send_headers, data=json.dumps({
#     "chat_id": "oc_9f176f68b3a8435583dc6ec8d0abe513",
#     "msg_type": "text",
#     "content": {
#         "text": "text content"
#     }
# })).text)

# print(json.loads(requests.post("http://api.apishop.net/common/joke/getJokesByRandom", data={
#             "apiKey": "5ZULlnD5f01345b094672e3ea5b6f7e1d299e1777930ac3",
#             "pageSize": "1"
#         }).text)['result'][0]['content'])

# _thread.start_new_thread(gen_tenant_token, (oapi_session,))
# time.sleep(2)

# print(get_group_members("oc_26d4a527179347e43bc3e32f82b7bf67"))
# print(gen_auth_code_url())
# # fef931ad85156dbb2cc1df4c5d3132d418d66d0b
# gen_tenant_token()
# gen_app_token()
# print(oapi_session.get(gen_auth_code_url()).text)

gen_tenant_token()
print(send_message("oc_26d4a527179347e43bc3e32f82b7bf67","测试哦"))