
import requests

requests.packages.urllib3.disable_warnings()

class Authentication_helper:

    def __init__(self, base_url):
        self.base_url = base_url

    def _url(self, path):
        return '%s%s' % (self.base_url, path)

    def req_sessionid(self):
        aut_body = {
            "login": "golubenkov_test@mail.ru",
            "password": "igor-igor"
            }
        aut_headers = {
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8"
            }
        return requests.post(self._url('auth/local'), json=aut_body, headers=aut_headers, verify=False)

    def req_code(self, headers_1):
        oauth_headers = {
            "X-Session-Id": ses_id,
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8"
            }
        oauth_body = {
            "clientId": 0,
            "credentials": {"id": ["main","accounts","groups"]
                }
            }
        return requests.post(self._url('oauth/code'), json=oauth_body, headers=headers_1, verify=False)

    def req_oauth_token(self, ses_id, ses_code):
        oauth_token_headers = {
            "X-Session-Id": ses_id,
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8"
            }
        oauth_token_body = {
                "clientId": "0",
                "clientSecret": "@Mqb8Xh7m5N5~eW",
                "grantType": "code",
                "code": ses_code,
                "refreshToken": "null"
                }
        return requests.post(self._url('oauth/token'), json=oauth_token_body, headers=oauth_token_headers, verify=False)
