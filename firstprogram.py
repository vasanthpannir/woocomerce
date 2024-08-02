from woocommerce import API

wcapi = API(
    url="http://localhost:10004/",
    consumer_key="ck_57e2ccac8d36726b209a87d68da2040edd153ace",
    consumer_secret="cs_270cf1af6714389540e588daffb98377b712f80d",
    version="wc/v3"
)
r = wcapi.get("products")
print(r.json())
from pprint import pprint
pprint(r.json())