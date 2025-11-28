
import pytest
from utils.constans import TOKEN_INVALID, ID_BOARD_NOT_EXISTS , ID_BOARD_EMPTY ,ID_BOARD_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests



@pytest.mark.board
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "test_020: eliminar_tablero_con_token_valido",
          "test_021: eliminar_tablero_con_token_invalidos"
     ])

def test_elimimar_tablero(get_token,use_fixture,token_value,expected_status,id_board):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{id_board}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_board , expected_status",[
        pytest.param(ID_BOARD_NOT_EXISTS,404,
                   id="test_022: eliminar_tablero_con_id_tablero_no_existente"),
        
        pytest.param(ID_BOARD_EMPTY,400,
                   marks=pytest.mark.xfail(reason="BUG005: Código de respuesta incorrecto de (404) al solicitar eliminar un tablero sin especificar su identificador (ID)"),
                   id="test_023: eliminar_tablero_con_id_tablero_vacio"),
        
        pytest.param(ID_BOARD_INVALID_STRING,400,
                   id="TC024: delete_board_with_invalid_id_type")

    ])

def test_eliminar_tablero_por_id_tablero(get_token,id_board,expected_status):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{id_board}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA} '}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status==404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)






