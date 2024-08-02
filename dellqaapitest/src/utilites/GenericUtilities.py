import random
import string
import logging as logger


def generate_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'supersqa.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain
    password_length = 20
    password_string = ''.join(random.choices(string.ascii_lowercase, k=password_length))
    random_info = {'email':email,'password':password_string}
    return random_info

