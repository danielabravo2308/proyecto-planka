import requests
from config import BASE_URI , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200 ,assert_status_code_401
import pytest


@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_delete_card_valid_token(get_token,post_card):
  ID_CARD = post_card
  TOKEN_PLANKA = get_token
  url = f"{BASE_URI}/cards/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_delete_card_invalid_token(post_card): 
  ID_CARD = post_card
  url = f"{BASE_URI}/cards/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_401(response)


