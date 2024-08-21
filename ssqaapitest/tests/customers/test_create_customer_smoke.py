import pytest
import logging as logger
from ssqaapitest.src.utilities.genericutilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customer_helpers import CustomerHelper
from ssqaapitest.src.DAO.customer_dao import CustomerDAO

@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Test:Create new customer with email and password")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']
    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)
    # verify email in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email.Email:{email}"
    assert cust_api_info['first_name'] == '', f"Create Customer api returned value for first_name"
    f"but it should be empty"
    # verify customer is created in database

    cust_dao = CustomerDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    import pdb;pdb.set_trace()




