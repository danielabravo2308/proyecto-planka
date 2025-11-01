import requests
from config import BASE_URI
from src.assertions.status_code import assert_status_code_200

def test_get_users(get_token):
    url = f"{BASE_URI}/users"
    TOKEN_PLANKA = get_token
    print(TOKEN_PLANKA)
    payload = {}
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)
