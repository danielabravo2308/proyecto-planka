import requests
import json
import jsonschema
import pytest
from config import BASE_URI , TOKEN_INVALID , ID_PROJECT1
from src.assertions.status_code import assert_status_code_200 , assert_status_code_401, assert_status_code_400
from src.resources.payloads.project_payloads import PAYLOAD_BOARD_CREATE , PAYLOAD_BOARD_EMPTY_NAME,PAYLOAD_BOARD_EMPTY_POSITION,PAYLOAD_BOARD_EMPTY
from src.resources.schemas.project_schema import SCHEMA_BOARD_OUTPUT



@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_post_board_valid_token(get_token):
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation 
def test_TC002_post_board_invalid_token():
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}',
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
def test_TC003_post_board_empty_name(get_token):
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_EMPTY_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)
    


@pytest.mark.project_management
@pytest.mark.functional_negative
def test_TC004_post_board_empty_position(get_token):
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_EMPTY_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
def test_TC005_post_board_empty_position_and_name(get_token):
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.schema_validation
def test_TC006_post_board_validation_schema_output(get_token):
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)

    assert_status_code_200(response)
    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_BOARD_OUTPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")

    

