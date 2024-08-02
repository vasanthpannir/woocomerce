from dellqaapitest.src.utilites.GenericUtilities import generate_email_and_password


class CustomerHelper(object):

    def __init__(self):
        pass

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_email_and_password()
        if not password:
            password = 'Password1'
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        return True
