
from test_cognita import Authentication_helper

base_req = Authentication_helper('https://id.test.cognita.ru/api/')

resp = base_req.req_sessionid()
ses_id = resp.json()['sessionId']

def test_get_sessionid():
        assert resp.status_code == 200, "проверка статуса сервера"
        assert len(ses_id) > 0, "проверка получения session Id"
        if resp.status_code == 200:
                print("проверка получения sessionId пройдена")

resp = base_req.req_code(ses_id)

def test_get_code():
        pass











