import pytest
import logging as logger
from dellqaapitest.src.utilites.GenericUtilities import generate_email_and_password
from dellqaapitest.src.Helpers.customer_helper import CustomerHelper


@pytest.mark.tcid111
def test_create_customer_only_email_password():
    logger.info("Test:Create a new customer with email and password")
    rand_info = generate_email_and_password()
    email = rand_info['email']
    password = rand_info['password']
    #payload
    payload = {'email':email,'password': password}

    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email,password=password)

    import pdb; pdb.set_trace()



