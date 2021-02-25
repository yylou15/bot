import json
import time

from api import oapi_session

app_id = "cli_9f67c7eaccb0500b"
app_secret = "opy4NazX54hx8W0CRj4cqdK1eF0oQBGw"


def gen_tenant_token():
    while True:
        token_res = json.loads(
            oapi_session.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/",
                              data=json.dumps({
                                  "app_id": app_id,
                                  "app_secret": app_secret
                              })).text)
        oapi_session.headers['Authorization'] = "Bearer {}".format(token_res['tenant_access_token'])
        time.sleep(30 * 60)


def gen_app_token() -> str:
    token_res = json.loads(
        oapi_session.post("https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/",
                          data=json.dumps({
                              "app_id": app_id,
                              "app_secret": app_secret
                          })).text)
    oapi_session.headers['Authorization'] = "Bearer {}".format(token_res['app_access_token'])
    return token_res['app_access_token']


def gen_auth_code_url():
    return "https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={}&app_id={}".format(
        "http%3A%2F%2Fblog.lou-yy.com", app_id
    )


def gen_user_token(app_token: str) -> str:
    token_res = json.loads(
        oapi_session.post("https://open.feishu.cn/open-apis/authen/v1/access_token"
                          , data=json.dumps({
                "app_access_token": app_token,
                "grant_type": "authorization_code",
                "code": "xMSldislSkdK"
            })).text
    )
    print(token_res)
