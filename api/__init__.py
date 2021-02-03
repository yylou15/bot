import requests

send_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer t-1",
}
oapi_session = requests.Session()
oapi_session.headers = send_headers
