

from first_test import*

req = Authentication_helper_2('https://id.test.cognita.ru/api/')

#resp = req.req_sessionId()

def get_json():
    return resp.json()

def get_status_code():
    return resp.status_code

#code = get_status_code()
#json = get_json()
#ses_id_2 = get_json()['sessionId']

resp = req.req_sessionId()

print(req.get_json_sesid())
print(get_status_code())
print(get_json())

