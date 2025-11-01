import requests
import pytest
from config import BASE_URI , TOKEN_INVALID , ID_BOARD2
from src.assertions.status_code import assert_status_code_200, assert_status_code_401


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_delete_board_valid_token(get_token,post_test_board):
    TOKEN_PLANKA = get_token
    ID_BOARD =  post_test_board
    url = f"{BASE_URI}/boards/{ID_BOARD}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_200(response)



@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_delete_board_invalid_token():
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_401(response)