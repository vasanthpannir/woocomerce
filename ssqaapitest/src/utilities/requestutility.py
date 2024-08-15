from ssqaapitest.src.configs.host_config import API_HOST
from ssqaapitest.src.utilities.credentials_utility import CredentialsUtility
from requests_oauthlib import OAuth1
import requests
import os
import json



class RequestsUtility(object):
    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        # import pdb;pdb.set_trace()
        self.auth = OAuth1(wc_creds['wc_key'],wc_creds['wc_secrect'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        # import pdb;pdb.set_trace()
        if not headers:
            headers = {"content-type": "application/json"}
        url = self.base_url + endpoint
        import json
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers,auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code),\
        f"Expected status code {expected_status_code} but actual {self.status_code}"
        return rs_api.json()


