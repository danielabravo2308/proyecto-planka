
import pytest
from utils.constans import TOKEN_INVALID 
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD,PAYLOAD_CREATE_CARD_TYPE_EMPTY,PAYLOAD_CREATE_CARD_POSITION_EMPTY,PAYLOAD_CREATE_CARD_NAME_EMPTY,PAYLOAD_CREATE_CARD_TYPE_PROJECT,PAYLOAD_CREATE_CARD_TYPE_STORY , PAYLOAD_CREATE_CARD_TYPE_INVALID,PAYLOAD_CREATE_CARD_POSITION_INVALID,PAYLOAD_CREATE_CARD_NAME_INVALID,PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS
from src.resources.schemas.card_schema import SCHEMA_CARD_PAYLOAD_INPUT
from src.routes.endpoint import EndpointPlanka
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
from src.routes.request import PlankaRequests


@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.parametrize(
    "use_fixture,token_value,expected_status",
    [(True,None,200),
     (False,TOKEN_INVALID,401)
    ],
    ids=[
        "test_001: crear_tarjeta_con_token_valido",
        "test_002: crear_tarjeta_con_token_invalido"
    ])

def test_crear_tarjeta(setup_card,use_fixture,token_value,expected_status,id_list):
    get_token, created_cards = (setup_card if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_cards.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)


    

@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
def test_003_validar_esquema_de_entrada_de_datos_al_crear_tarjeta(setup_card,id_list):
    get_token,created_cards = setup_card
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_CARD, SCHEMA_CARD_PAYLOAD_INPUT)
    created_cards.append(response.json())


   
@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [(PAYLOAD_CREATE_CARD_TYPE_PROJECT,200),
     (PAYLOAD_CREATE_CARD_TYPE_STORY,200),
     (PAYLOAD_CREATE_CARD_TYPE_EMPTY,400),
     (PAYLOAD_CREATE_CARD_TYPE_INVALID,400)
    ],
    ids=[
        "test_004: crear_tarjeta_con_campo_tipo_projecto",
        "test_005: crear_tarjeta_con_campo_tipo_historia",
        "test_006: crear_tarjeta_con_campo_tipo_empty",
        "test_007: crear_tarjeta_con_campo_tipo_invalido" 
    ])

def test_crear_tarjeta_con_tipo_de_tarjeta(setup_card,payload,expected_status,id_list):
    get_token,created_cards = setup_card
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==200:
        AssertionStatusCode.assert_status_code_200(response)
        created_cards.append(response.json())
    else:
        AssertionStatusCode.assert_status_code_400(response)
    


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [
        pytest.param(PAYLOAD_CREATE_CARD_POSITION_EMPTY,400,
                   id="test_008: crear_tarjeta_con_campo_posicion_vacio"),

        pytest.param(PAYLOAD_CREATE_CARD_POSITION_INVALID,400,
                  id="test_009: crear_tarjeta_con_campo_posicion_invalido"),

        pytest.param(PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,400,
                  id="test_010: crear_tarjeta_con_campo_posicion_valor_negativo"),

        pytest.param( PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS,400,
                 marks=pytest.mark.xfail(reason="BG006: El campo position permite ingresar numeros sin limite de digitos"),
                 id="test_011: crear_tarjeta_con_campo_posicion_digitos_excedidos")
    ])

def test_crear_tarjeta_con_campo_posicion(get_token,payload,expected_status,id_list):
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)

    


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        pytest.param(PAYLOAD_CREATE_CARD_NAME_EMPTY,400,
                   id="test_012: crear_tarjeta_con_campo_nombre_vacio"),

        pytest.param(PAYLOAD_CREATE_CARD_NAME_INVALID,400,
                  marks=pytest.mark.xfail(reason="BUG007: El campo name permite ingresar valores numericos"),
                  id="test_013: crear_tarjeta_con_campo_nombre_invalido")
    ])

def test_crear_tarjeta_con_campo_nombre(get_token,payload,expected_status,id_list):
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)
    
    
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "url_id_list , expected_status", [
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_NOT_EXISTS.value,404,
                   id="test_014: crear_tarjeta_con_id_lista_inexistente"),
        
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_EMPTY.value,400,
                   marks=pytest.mark.xfail(reason="BUG008: Código HTTP incorrecto se retorna 404 en lugar de 400 al consultar un recurso vacio"),
                   id="test_015: crear_tarjeta_con_id_lista_vacia"),
        
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_INVALID.value,400,
                   id="test_016: crear_tarjeta_con_id_lista_invalido"),

    ])

def test_crear_tarjeta_por_id_lista(get_token,url_id_list,expected_status):
    url = url_id_list
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)
    if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
    else:
        AssertionStatusCode.assert_status_code_400(response)

    