

import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.project_schema import SCHEMA_OUTPUT_GET_PROJECTS
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
from src.routes.request import PlankaRequests



@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
def test_009_obtener_proyecto_con_token_valido(get_token):
   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.get(url,headers)
   log_request_response(url, response, headers)
   AssertionStatusCode.assert_status_code_200(response)
   

@pytest.mark.project_management
@pytest.mark.functional_negative
def test_010_obtener_proyecto_con_token_invalido():
   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
   response = PlankaRequests.get(url,headers)
   log_request_response(url, response, headers)
   AssertionStatusCode.assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.regression
def test_011_validar_esquema_de_salida_al_obtener_proyecto(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_schema_output_payload(response , SCHEMA_OUTPUT_GET_PROJECTS)

   

@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.performance
def test_012_validar_tiempo_de_respuesta_al_obtener_proyecto(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}    
      response = PlankaRequests.get(url,headers)
      log_request_response(url, response, headers)
      assert_response_time(response)
      
