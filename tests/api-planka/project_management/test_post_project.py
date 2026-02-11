import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE 
from src.resources.schemas.project_schema import SCHEMA_INPUT_CREATE_PROJECT,SCHEMA_OUTPUT_CREATE_PROJECT
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
def test_001_crear_proyecto_con_token_valido(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_negative
def test_002_crear_proyecto_con_token_invalido(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_401(response)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
def test_003_validar_esquema_de_salida_al_crear_proyecto(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_schema_output_payload(response , SCHEMA_OUTPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
def test_004_validar_esquema_de_entrada_al_crear_proyecto(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_schema_input_payload(PAYLOAD_PROJECT_CREATE,SCHEMA_INPUT_CREATE_PROJECT)
    created_projects.append(response.json())

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.parametrize(
    "type,name", [
        ("", "Proyecto Nuevo en tipo vacio"),
        ("other", "Mi Proyecto")
    ],

    ids=[
        "crear proyecto con el campo type vacio",
        "crear proyecto con el campo type no existente",
    ])

def test_005_crear_proyecto_con_el_campo_tipo_invalido(get_token,type,name):
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    payload = {"type": type,"name": name}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.parametrize(
    "type,name", [
        ("shared", "Mi Proyecto en type shared"),
        ("private", "Mi Proyecto en type private")
    ],

    ids=[
        "crear proyecto con el campo type shared",
        "crear proyecto con el campo type private"
    ])

def test_006_crear_proyecto_con_el_campo_tipo_valido(setup_project,type,name):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    payload = {"type": type,"name": name}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())
   
    


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.parametrize(
    "type,name",
    [
      pytest.param("shared","",
                   id="crear proyecto con el campo nombre vacio"),

      pytest.param("shared",1234,
                  marks=pytest.mark.xfail(reason="BUG014: El campo nombre del proyecto permite entradas numéricas",run=True),
                  id=" crear proyecto con el campo nombre de valor numérico"
        )
    ])

def test_007_crear_proyecto_con_el_campo_nombre_invalido(get_token,type,name):
   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {get_token}'}
   payload = {"type": type,"name": name}
   response = PlankaRequests.post(url,headers,payload)
   log_request_response(url, response, headers, payload)
   AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.project_management
@pytest.mark.functional_positive
def test_008_crear_proyecto_con_el_campo_nombre_valido(setup_project):  
    url = EndpointPlanka.BASE_PROJECTS.value
    get_token , created_projects = setup_project
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())


   
   
   

