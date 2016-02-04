

import requests

requests.packages.urllib3.disable_warnings()

class Authentication_helper:

    def __init__(self, base_url):
        self.base_url = base_url

    def req_post(self, url_lead, body_req, headers_lead):
        return requests.post(url=url_lead, json=body_req, headers=headers_lead, verify=False)
