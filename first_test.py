
import requests
from two_test import Authentication_helper

class Authentication_helper_2:

    def __init__(self, base_url):
        self.base_url = base_url
        self.auth = Authentication_helper(self.base_url)
        self.first_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-us,en;q=0.8",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            }
        self.aut_body = {
            "login": "golubenkov_test@mail.ru",
            "password": "igor-igor"
            }
        self.url_aut = 'auth/local'

    ses_id = 0
    req_json = 0
    resp = 0

    def _url(self, path):
        return '%s%s' % (self.base_url, path)

    def req_sessionId(self):
        return self.auth.req_post(self._url('auth/local'), self.aut_body, self.first_headers)

    def get_json_sesid(self):
        Authentication_helper_2.resp = self.req_sessionId().json()
        #Authentication_helper_2.ses_id = self.req_sessionId.json

    def get_ses_id(self):
        return Authentication_helper_2.resp[]

    def req_get_code(self):
        pass

'''
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
'''