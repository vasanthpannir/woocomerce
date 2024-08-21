import pymysql
from pymysql import cursors,connect
from ssqaapitest.src.utilities.credentials_utility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.hosts = 'localhost'

    def create_connection(self):
        connection = connect(host=self.hosts, user=self.creds['db_user'],
                             password=self.creds['db_password'], port=10005)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()

        except Exception as e:
            raise Exception(f"Failed running sql:{sql} \n.Error:{str(e)}")
        finally:
            conn.close()

        return rs_dict

