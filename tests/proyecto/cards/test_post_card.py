import requests
import json
import pytest
import jsonschema
from config import BASE_URI , TOKEN_INVALID , ID_LIST2
from src.assertions.status_code import assert_status_code_200 ,assert_status_code_400 ,assert_status_code_401
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_CARD , PAYLOAD_CREATE_CARD_TYPE_EMPTY,PAYLOAD_CREATE_CARD_POSITION_EMPTY,PAYLOAD_CREATE_CARD_NAME_EMPTY 
from src.resources.schemas.project_schema import SCHEMA_CARD_PAYLOAD_INPUT


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_post_card_valid_token(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)
    

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_post_card_invalid_token():
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)
    
@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC003_post_card_validation_payload_input(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(PAYLOAD_CREATE_CARD, schema= SCHEMA_CARD_PAYLOAD_INPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC004_post_card_validate_attribute_type_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC005_post_card_validate_attribute_position_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
def test_TC006_post_card_validate_attribute_name_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)