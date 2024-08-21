from ssqaapitest.src.utilities.dbutility import DBUtility


class CustomerDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        import pdb; pdb.set_trace()
