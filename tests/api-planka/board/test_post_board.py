
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE,PAYLOAD_BOARD_EMPTY_NAME,PAYLOAD_BOARD_EMPTY_POSITION,PAYLOAD_BOARD_NAME_VALUE_NUMBER,PAYLOAD_BOARD_POSITION_NEGATIVE,PAYLOAD_BOARD_POSITION_INVALID_TYPE,PAYLOAD_BOARD_POSITION_LARGE
from src.resources.schemas.board_schema import SCHEMA_BOARD_OUTPUT
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
        "test_001: crear_tablero_con_token_valido",
        "test_002: crear_tablero_con_token_invalido"
    ])

def test_crear_tablero(setup_board,use_fixture,token_value,expected_status,id_project):
    get_token, created_boards = (setup_board if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url, response, headers, PAYLOAD_BOARD_CREATE)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_boards.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [
        pytest.param(PAYLOAD_BOARD_EMPTY_NAME,400,
                   id="test_003: crear_tablero_con_campo_nombre_vacio"),

        pytest.param(PAYLOAD_BOARD_NAME_VALUE_NUMBER,400,
                  marks=pytest.mark.xfail(reason="BUG001: El atributo nombre permite entradas de valor numérico"),
                  id="test_004: crear_tablero_con_campo_nombre_valor_numerico")
    ])

def test_crear_tablero_por_campo_nombre(get_token,payload,expected_status,id_project):
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if  expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)
 


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [
       pytest.param(PAYLOAD_BOARD_EMPTY_POSITION,400,
                   id="test_005: crear_tablero_con_campo_posicion_vacio"),

        pytest.param(PAYLOAD_BOARD_POSITION_NEGATIVE,400,
                  id="test_006: crear_tablero_con_campo_posicion_valor_negativo"),
        
        pytest.param(PAYLOAD_BOARD_POSITION_INVALID_TYPE,400,
                   id="test_007: crear_tablero_con_campo_posicion_valor_invalido_tipo"),

        pytest.param(PAYLOAD_BOARD_POSITION_LARGE,400,
                  marks=pytest.mark.xfail(reason="BUG002: El campo position no tiene un valor limite de cantidad de digitos"),
                  id="test_008: crear_tablero_con_campo_posicion_con_valor_numerico_grande")

    ])

def test_crear_tablero_por_campo_posicion(get_token,payload,expected_status,id_project):
       url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
       headers = {'Authorization': f'Bearer {get_token}'}
       response = PlankaRequests.post(url,headers,payload)
       log_request_response(url, response, headers, payload)
       if  expected_status==400:
           AssertionStatusCode.assert_status_code_400(response)
     

       

@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "url_id_project , expected_status", [
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_NOT_EXISTS.value,404,
                     marks=pytest.mark.xfail(reason="BUG003:Código de respuesta incorrecto de (400) al solicitar crear tablero especificando el identificador (ID) de proyecto no existente"),

                   id="test_009: crear_tablero_con_id_proyecto_no_existente"),
        
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_EMPTY.value,404,
                   id="test_010: crear_tablero_con_id_proyecto_vacio"),
        
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_INVALID.value,400,
                   id="test_011: crear_tablero_con_id_proyecto_valor_invalido_tipo")
    ])

def test_crear_tablero_por_id_proyecto(get_token,url_id_project,expected_status):
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url_id_project,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url_id_project, response, headers, PAYLOAD_BOARD_CREATE)
    if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
    else:
        AssertionStatusCode.assert_status_code_400(response)




def test_012_validar_esquema_de_respuesta_al_crear_tablero(setup_board,id_project):
    get_token,created_boards = setup_board
    TOKEN_PLANKA = get_token
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url, response, headers, PAYLOAD_BOARD_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_BOARD_OUTPUT)
    created_boards.append(response.json())

 
  