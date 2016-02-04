


import requests

requests.packages.urllib3.disable_warnings()

def _url(path):
    return 'https://id.test.cognita.ru/api/' + path

def req_get_sessionid():
    aut_body = {
            "login": "golubenkov_test@mail.ru",
            "password": "igor-igor"
            }
    aut_headers = {
    "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8"
    }
    return requests.post(_url('auth/local'), json=aut_body, headers=aut_headers, verify=False)

ses_id = req_get_sessionid().json()['sessionId']

def get_code():
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
    return requests.post(_url('oauth/code'), json=oauth_body, headers=oauth_headers, verify=False)

