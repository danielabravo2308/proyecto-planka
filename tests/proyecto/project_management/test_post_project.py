import requests
import json
import jsonschema
import pytest
from config import BASE_URI , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200,assert_status_code_400,assert_status_code_401
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE , PAYLOAD_PROJECT_CREATE_NAME_EMPTY , PAYLOAD_PROJECT_CREATE_DESCRIPTION_EMPTY
from src.resources.schemas.project_schema import SCHEMA_OUTPUT_CREATE_PROJECT,SCHEMA_INPUT_CREATE_PROJECT


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_post_project_valid_token(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
def test_TC002_post_project_invalid_no_name(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
def test_TC003_post_project_invalid_no_description(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_DESCRIPTION_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC004_post_project_invalid_token():
    url = f"{BASE_URI}/projects"
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}',
    'Content-Type': 'application/json'
    }
     
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.schema_validation
def test_TC005_post_validate_payload_output(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token 
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_OUTPUT_CREATE_PROJECT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.payload_validation
def test_TC006_post_validate_payload_input(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    headers = {
        'Authorization': f'Bearer {TOKEN_PLANKA}',
        'Content-Type': 'application/json'
        }
    
    response = requests.post(url,headers=headers,json=PAYLOAD_PROJECT_CREATE)
    assert_status_code_200(response)


    try:
        jsonschema.validate(PAYLOAD_PROJECT_CREATE, schema= SCHEMA_INPUT_CREATE_PROJECT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


