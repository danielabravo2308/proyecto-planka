import requests
import pytest
import jsonschema
from config import BASE_URI , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200 , assert_status_code_401
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.project_schema import SCHEMA_OUTPUT_GET_PROJECTS


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_get_project_valid_token(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_get_project_invalid_token():
    url = f"{BASE_URI}/projects"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url,headers=headers)
    assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.schema_validation
def test_TC003_get_project_validate_schema_output(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    headers = {
          'Authorization': f'Bearer {TOKEN_PLANKA}'
    }    
    response = requests.get(url,headers=headers)
    assert_status_code_200(response)
    

    try:
            jsonschema.validate(instance=response.json(), schema= SCHEMA_OUTPUT_GET_PROJECTS)
    except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")



@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.response_time
def test_TC004_get_project_validate_response_time(get_token):
      url = f"{BASE_URI}/projects"
      TOKEN_PLANKA = get_token
      headers = {
            'Authorization': f'Bearer {TOKEN_PLANKA}'
      }    
      
      response = requests.get(url,headers=headers)
      assert_response_time(response)
      