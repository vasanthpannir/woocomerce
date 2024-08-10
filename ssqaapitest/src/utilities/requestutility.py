from ssqaapitest.src.configs.host_config import API_HOST
import requests
import os
from requests_oauthlib import OAuth1
import json


class RequestsUtility(object):
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        self.auth = OAuth1("ck_116d7456d3d494bb31efb8a697b252fd8ddbbadd","cs_04de687534672772a18ef1dc98449643c5213860")

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"content-type": "application/json"}
        url = self.base_url + endpoint
        import json
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code),\
        f"Expected status code {expected_status_code} but actual {self.status_code}"
        return rs_api.json()

        import pdb;
        pdb.set_trace()
