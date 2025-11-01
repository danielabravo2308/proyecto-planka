import requests
import json
import pytest
from config import BASE_URI
from src.assertions.status_code import assert_status_code_200
#from src.payloads.user_management_payloads import PAYLOAD_USER_CREATE,PAYLOAD_USER_CREATE_FAKER
from src.helpers.users_faker import generate_faker_user_payload


# @pytest.mark.user_management
# @pytest.mark.functional_positive

# def test_TC001_post_users_valid(get_token):
#     url = f"{BASE_URI}/users"
#     TOKEN_PLANKA = get_token
#     payload = json.dumps(generate_faker_user_payload)
#     headers = {
#     'Authorization': f'Bearer {TOKEN_PLANKA}',
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     assert_status_code_200(response)



