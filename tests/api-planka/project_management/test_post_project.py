import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE , PAYLOAD_PROJECT_CREATE_NAME_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_SHARED,PAYLOAD_PROJECT_CREATE_TYPE_INVALID,PAYLOAD_PROJECT_CREATE_NAME_NUMBER
from src.resources.schemas.project_schema import SCHEMA_INPUT_CREATE_PROJECT,SCHEMA_OUTPUT_CREATE_PROJECT
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.parametrize(
    "use_fixture,token_value,expected_status",
    [(True,None,200),
     (False,TOKEN_INVALID,401)
    ],
    ids=[
        "test_001: crear_proyecto_con_token_valido",
        "test_002: crear_proyecto_con_token_invalido"
    ])

def test_crear_proyecto_con_token(setup_project,use_fixture,token_value,expected_status):
    get_token, created_projects = (setup_project if use_fixture else (token_value, []))

    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_projects.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.regression
@pytest.mark.functional_positive
def test_003_validar_esquema_de_salida_al_crear_proyecto(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token 
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response , SCHEMA_OUTPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.regression
@pytest.mark.functional_positive
def test_004_validar_esquema_de_entrada_al_crear_proyecto(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_PROJECT_CREATE,SCHEMA_INPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        (PAYLOAD_PROJECT_CREATE, 200),
        (PAYLOAD_PROJECT_CREATE_TYPE_SHARED, 200),
        (PAYLOAD_PROJECT_CREATE_TYPE_EMPTY, 400),
        (PAYLOAD_PROJECT_CREATE_TYPE_INVALID, 400)
    ],

    ids=[
        "test_005 : crear_proyecto_con_el_campo_tipo_privado",
        "test_006 : crear_proyecto_con_el_campo_tipo_publico",
        "test_007 : crear_proyecto_con_el_campo_tipo_vacio",
        "test_008 : crear_proyecto_con_el_campo_tipo_invalido",
    ])

def test_crear_proyecto_con_el_campo_tipo(setup_project,payload,expected_status):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}

    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_projects.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_400(response)
    


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload,expected_status",
    [
      pytest.param(PAYLOAD_PROJECT_CREATE_NAME_EMPTY,400,
                   id="test_009: crear_proyecto_con_el_campo_nombre_vacio"),

      pytest.param(PAYLOAD_PROJECT_CREATE_NAME_NUMBER,400,
                  marks=pytest.mark.xfail(reason="BUG014: El campo nombre del proyecto permite entradas numéricas",run=True),
                  id="test_010: crear_proyecto_con_el_campo_nombre_de_valor_numerico"
        )
    ])

def test_crear_proyecto_con_el_campo_nombre(get_token,payload,expected_status):
   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,payload)
   log_request_response(url, response, headers, payload)
   if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)
   
   
   

