import requests
import pytest
import jsonschema
from config import BASE_URI , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200 , assert_status_code_401


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation

def test_TC001_delete_project_valid_token(get_token, create_test_project):
    ID_PROJECT = create_test_project
    url = f"{BASE_URI}/projects/{ID_PROJECT}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.delete(url, headers=headers)
    assert_status_code_200(response)

    
@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_delete_project_invalid_token(create_test_project):
   ID_PROJECT = create_test_project
   url = f"{BASE_URI}/projects/{ID_PROJECT}"
   headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

   response = requests.delete(url,headers=headers)
   assert_status_code_401(response)




   