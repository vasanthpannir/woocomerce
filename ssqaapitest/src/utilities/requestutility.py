from ssqaapitest.src.configs.host_config import API_HOST
from ssqaapitest.src.utilities.credentials_utility import CredentialsUtility
from requests_oauthlib import OAuth1
import logging as logger
import requests
import os
import json


class RequestsUtility(object):
    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secrect'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status Code." \
                                                                 f"Expected {self.expected_status_code},Actual status code:{self.status_code}," \
                                                                 f"URL:{self.url},Response Json:{self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"content-type": "application/json"}
        self.url = self.base_url + endpoint
        import json
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        # import pdb;pdb.set_trace()
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"API response:{self.rs_json}")
        return self.rs_json