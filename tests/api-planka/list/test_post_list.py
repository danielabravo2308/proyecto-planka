
import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST,PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_CLOSED,PAYLOAD_CREATE_LIST_EMPTY_TYPE,PAYLOAD_CREATE_LIST_EMPTY_POSITION,PAYLOAD_CREATE_LIST_EMPTY_NAME,PAYLOAD_CREATE_LIST_INVALID_TYPE,PAYLOAD_CREATE_LIST_INVALID_POSITION ,PAYLOAD_CREATE_LIST_INVALID_NAME,PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS
from src.resources.schemas.list_schema import SCHEMA_CREATE_LIST_OUTPUT,SCHEMA_LIST_PAYLOAD_INPUT
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
from src.routes.request import PlankaRequests


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.parametrize(
    "use_fixture,token_value,expected_status",
    [(True,None,200),
     (False,TOKEN_INVALID,401)
    ],
    ids=[
        "test_001: crear_lista_con_token_valido",
        "test_002: crear_lista_con_token_invalido"
    ])

def test_crear_lista(setup_list,use_fixture,token_value,expected_status,id_board):
    get_token, created_lists = (setup_list if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_lists.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        (PAYLOAD_CREATE_LIST_TYPE_ACTIVE, 200),
        (PAYLOAD_CREATE_LIST_TYPE_CLOSED, 200),
        (PAYLOAD_CREATE_LIST_EMPTY_TYPE, 400),
        (PAYLOAD_CREATE_LIST_INVALID_TYPE, 400)
    ],

    ids=[
        "test_003 : crear_lista_con_campo_tipo_activo",
        "test_004 : crear_lista_con_campo_tipo_cerrado",
        "test_005 : crear_lista_con_campo_tipo_vacio",
        "test_006 : crear_lista_con_campo_tipo_invalido"
    ])

def test_crear_lista_con_campo_tipo(setup_list,payload,expected_status,id_board):
    get_token, created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}

    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_lists.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_400(response)
    



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload,expected_status",
    [
        pytest.param(PAYLOAD_CREATE_LIST_EMPTY_POSITION,400,
                   id="test_007: crear_lista_con_campo_posicion_vacio"),

        pytest.param(PAYLOAD_CREATE_LIST_INVALID_POSITION,400,
                  id="test_008: crear_lista_con_campo_posicion_invalido"),


        pytest.param(PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,400,
                  id="test_009: crear_lista_con_campo_posicion_valor_negativo"),

        pytest.param(PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS,400,
                 marks=pytest.mark.xfail(reason="BUG011: El campo position permite ingresar numeros sin limite de digitos "),
                  id="test_010: crear_lista_con_campo_posicion_valor_sin_limite")

 ])

def test_crear_lista_con_campo_posicion(get_token,payload,expected_status,id_board):
   url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,payload)
   log_request_response(url, response, headers, payload)
   
   if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
        "payload,expected_status",
        [
            pytest.param(PAYLOAD_CREATE_LIST_EMPTY_NAME,400,
                    id="test_011: crear_lista_con_campo_nombre_vacio"),

            pytest.param(PAYLOAD_CREATE_LIST_INVALID_NAME,400,
                    marks=pytest.mark.xfail(reason="BUG012: El campo name permite ingresar valores numericos",run=True),
                    id="test_012: crear_lista_con_campo_nombre_invalido_valor_numerico")
        ])

def test_create_lista_con_campo_nombre(get_token,payload,expected_status,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
def test_013_validar_esquema_de_salida_al_crear_lista(setup_list,id_board):
    get_token,created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_CREATE_LIST_OUTPUT)
    created_lists.append(response.json())

   

@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
def test_014_validar_esquema_de_entrada_al_crear_lista(setup_list,id_board):
    get_token,created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_LIST,SCHEMA_LIST_PAYLOAD_INPUT)
    created_lists.append(response.json())

    

@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "url_id_board,expected_status",[
      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_NOT_EXISTS.value,404,
                   id="test_015: crear_lista_co_id_tablero_no_existente"),

      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_EMPTY.value,404,
                   id="test_016: crear_lista_con_id_tablero_vacio"),
      
      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_INVALID.value,400,
                   id="test_017: crear_lista_con_id_tablero_invalido")

   ])

def test_crear_lista_por_id_tablero(get_token,url_id_board,expected_status):
   url = url_id_board
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
   log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
   if expected_status==404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)

   
  