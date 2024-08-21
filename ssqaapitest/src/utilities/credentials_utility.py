
import os

class CredentialsUtility(object):
    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('wc_key')
        wc_secrect = os.environ.get('wc_secrect')

        if not wc_key or not wc_secrect:
            raise Exception("The API credentials WC_KEY and 'WC_SECRECT' must be in env variable")
        else:
            return {'wc_key': wc_key, 'wc_secrect': wc_secrect}

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The API credentials 'db_user' and 'db_password' must be in env variable")
        else:
            return {'db_user': db_user, 'db_password': db_password}
