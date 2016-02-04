
import requests

base_url = 'https://id.test.cognita.ru/api/'

first_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-us,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
}

requests.packages.urllib3.disable_warnings()
'''
url_requestor = '%s"url"'  % base_url
some_body = {}
some_headers = {}
name_request = requests.post(url_requestor, json=some_body, headers=some_headers, verify=False)
print("\nStatus_'name_request':", name_request.status_code)
print("Json_'name_request':", name_request.json())

url_register = '%sreg/register' % base_url
register_body = {
    "user":{
        "info":{
            "firstName":"easrg",
            "lastName":"sertg",
            "login":"123@777.test",
            "email":"123@777.test"
                },
        "email":"",
        "loginType":"email",
        "login":"123@777.test",
        "password":"123456"
            },
    "requestId":"56b066c52a4f092d0abbb0b3",
    "answer":"55"
    }
register = requests.post(url_register, json=register_body, headers=first_headers, verify=False)
print("\nStatus_register:", register.status_code)
print("Json_register:", register.json())
#print("Headers_register:", register.headers)
'''
url_aut = '%sauth/local' % base_url
aut_body = {
            "login": "golubenkov_test@mail.ru",
            "password": "igor-igor"
            }
aut = requests.post(url_aut, json=aut_body, headers=first_headers, verify=False, timeout=2)
print("\nStatus_aut:", aut.status_code)
print("Json_sessionId:", aut.json())
#print("Headers_aut:", aut.headers)

ses_id = aut.json()['sessionId']
print("\nSession_Id:", ses_id)

headers_X_Session_Id = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-us,en;q=0.8",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "X-Session-Id": ses_id,
            }

url_oauth = '%soauth/code' % base_url
oauth_body = {
        "clientId":0,
        "credentials": {"id": ["main","accounts","groups"]
        }
    }
oauth = requests.post(url_oauth, json=oauth_body, headers=headers_X_Session_Id, verify=False)
print("\nStatus_oauth:", oauth.status_code)
print("Json_code:", oauth.json())
#print("Headers_oauth:", oauth.headers)

ses_code = oauth.json()['code']
print("\nSession_code:", ses_code)

url_oauth_token = '%soauth/token'  % base_url
oauth_token_body = {
                "clientId": "0",
                "clientSecret": "@Mqb8Xh7m5N5~eW",
                "grantType": "code",
                "code": ses_code,
                "refreshToken": "null"
                    }
oauth_token = requests.post(url_oauth_token, json=oauth_token_body, headers=headers_X_Session_Id, verify=False)
print("\nStatus_oauth_token:", oauth.status_code)
print("Json_oauth_token:", oauth_token.json())
#print("Headers_oauth_token:", oauth_token.headers)

ses_token = oauth_token.json()['token']
print("\nSession_token:", ses_token)

ses_refreshToken = oauth_token.json()['refreshToken']
print("\nSession_refreshToken:", ses_refreshToken)

ses_refreshTokenExpirationDate = oauth_token.json()['refreshTokenExpirationDate']
print("\nSession_refreshTokenExpirationDate:", ses_refreshTokenExpirationDate)

secured_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-us,en;q=0.8",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
            "X-Access-Token": ses_token,
            "X-Session-Id": ses_id,
                }
'''
url_des_app = '%soauth/applications' % base_url
des_app = requests.get(url=url_des_app, verify=False)
print("\nStatus_des_app:", des_app.status_code)
print("Json_des_app:", des_app.json())
#print("Headers_des_app:", des_app.headers)

url_des_id = '%soauth/applications/2' % base_url
des_id = requests.get(url=url_des_id, verify=False)
print("\nStatus_des_id:", des_id.status_code)
print("Json_des_id:", des_id.json())
#print("Headers_des_appdes_app:", des_id.headers)

url_arr_service = '%soauth/scopes' % base_url
arr_service = requests.get(url=url_arr_service, verify=False)
print("\nStatus_arr_service:", arr_service.status_code)
print("Json_arr_service:", arr_service.json())
#print("Headers_arr_service:", arr_service.headers)

url_arr_name = '%soauth/scopes/id' % base_url
arr_name = requests.get(url=url_arr_name, verify=False)
print("\nStatus_arr_name:", arr_name.status_code)
print("Json_arr_name:", arr_name.json())
#print("Headers_arr_name:", arr_name.headers)
'''

url_user_me = '%susers/me' % base_url
user_me = requests.get(url=url_user_me, headers=secured_headers, verify=False)
print("\nStatus_user_me:", user_me.status_code)
print("Json_user_me:", user_me.json())
#print("Headers_user_me:", user_me.headers)

url_userme_accounts = '%susers/me/accounts' % base_url
userme_accounts = requests.get(url_userme_accounts, headers=secured_headers, verify=False)
print("\nStatususerme_accounts:", userme_accounts.status_code)
print("Json_userme_accountst:", userme_accounts.json())
#print("Headers_userme_get:", userme_get.headers)


def tampletes_post():
    url_some = '%s"url"' % base_url
    some_body = {}
    name_request = requests.post(url_some, json=some_body, headers=headers_X_Session_Id, verify=False)
    print("\nStatus_'name_request':", name_request.status_code)
    print("Json_'name_request':", name_request.json())

def tampletes_get():
    url_some = '%s"url"' % base_url
    name_request = requests.post(url_some, headers=headers_X_Session_Id, verify=False)
    print("\nStatus_'name_request':", name_request.status_code)
    print("Json_'name_request':", name_request.json())
