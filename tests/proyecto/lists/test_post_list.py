import requests
import json
import pytest
import jsonschema
from config import BASE_URI , ID_BOARD2 , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200 , assert_status_code_400,assert_status_code_401
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_LIST , PAYLOAD_CREATE_LIST_TYPE_ACTIVE , PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_CLOSED,PAYLOAD_CREATE_LIST_EMPTY_TYPE,PAYLOAD_CREATE_LIST_EMPTY_POSITION,PAYLOAD_CREATE_LIST_EMPTY_NAME
from src.resources.schemas.project_schema import SCHEMA_CREATE_LIST_OUTPUT,SCHEMA_LIST_PAYLOAD_INPUT



@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_post_list_valid_token(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_post_list_invalid_token():
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC003_post_list_attribute_type_active(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_ACTIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)



@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC004_post_list_attribute_type_closed(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_CLOSED)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC005_post_list_attribute_type_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC005_post_list_attribute_position_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC006_post_list_attribute_name_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.schema_validation
def test_TC007_post_list_schema_validation(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_CREATE_LIST_OUTPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.schema_validation

def test_TC008_post_list_validate_payload_input(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(PAYLOAD_CREATE_LIST, schema= SCHEMA_LIST_PAYLOAD_INPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")
