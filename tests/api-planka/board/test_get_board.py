
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.schemas.board_schema import SCHEMA_BOARD_OUTPUT2
from src.assertions.assertion_general import assert_response_time
from src.assertions.schema_assertion import AssertionSchemas
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
        "test_013: obtener_tablero_con_token_valido",
        "test_014: obtener_tablero_con_token_invalido"
    ])

def test_obtener_tablero(get_token,use_fixture,token_value,expected_status,id_board):
    TOKEN_PLANKA = (get_token if use_fixture else (token_value))

    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    print(f"Status code es Error?: {response.status_code}, Response: {response.text}")

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
    
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.regression
def test_015_validar_esquema_de_respuesta_al_obtener_tablero(get_token,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_BOARD_OUTPUT2)


   
@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.performance
def test_016_validar_tiempo_de_respuesta_al_obtener_tablero(get_token,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "url_id_board , expected_status", [
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_NOT_EXISTS.value,404,
                   id="test_017:obtener_tablero_con_id_tablero_no_existente"),

        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_EMPTY.value,400,
                   marks=pytest.mark.xfail(reason=" BUG004: La aplicación retorna código 200 y muestra un mensaje en HTML al dejar vacio el identificador (ID) tablero"),
                   id="test_018:obtener_tablero_con_id_tablero_vacio"),

        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_INVALID.value,400,
                   id="test_019:obtener_tablero_con_id_tablero_valor_invalido_tipo")    
    ])

def test_obtener_tablero_por_id_tablero(get_token,url_id_board,expected_status):
     url = url_id_board
     headers = {'Authorization': f'Bearer {get_token}'}
     response = PlankaRequests.get(url,headers)
     log_request_response(url, response, headers)
     if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
     else:
        AssertionStatusCode.assert_status_code_400(response)
     
