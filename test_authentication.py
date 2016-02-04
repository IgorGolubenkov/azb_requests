
from two_test import Authentication_helper

auth = Authentication_helper('https://id.test.cognita.ru/api/')

first_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-us,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
}
aut_body = {
            "login": "golubenkov_test@mail.ru",
            "password": "igor-igor"
            }

resp = auth.req_sessionid(aut_body, first_headers)

if resp.status_code != 200:
    raise ConnectionError('Status error: {}'.format(resp.status_code))
print('Get Session ID: {}'.format(resp.json()["sessionId"]), ",", 'Response JSON: {}'.format(resp.json()))

ses_id = resp.json()['sessionId']

headers_X_Session_Id = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-us,en;q=0.8",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "X-Session-Id": ses_id,
            }

oauth_body = {
            "clientId": 0,
            "credentials": {
                "id": ["main","accounts","groups"]
                }
            }

resp = auth.req_code(oauth_body, headers_X_Session_Id)

ses_code = resp.json()['code']

if resp.status_code != 200:
    raise ConnectionError('Status error: {}'.format(resp.status_code))
print('Get Code: {}'.format(ses_code), ",", 'Response JSON: {}'.format(resp.json()))

oauth_token_body = {
                "clientId": "0",
                "clientSecret": "@Mqb8Xh7m5N5~eW",
                "grantType": "code",
                "code": ses_code,
                "refreshToken": "null"
                }

resp = auth.req_oauth_token(oauth_token_body, headers_X_Session_Id)

ses_token = resp.json()["token"]

if resp.status_code != 200:
    raise ConnectionError('Status error: {}'.format(resp.status_code))
print('Get oauth Token: {}'.format(ses_token), ",", 'Response JSON: {}'.format(resp.json()))


