

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
@pytest.mark.functional_negative
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "test_011: obtener_proyecto_con_token_valido",
          "test_012: obtener_proyecto_con_token_invalido"
     ])

def test_obtener_proyecto(get_token,use_fixture,token_value,expected_status):
   TOKEN_PLANKA =get_token if use_fixture else token_value

   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.get(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)
   


@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.regression
def test_013_validar_esquema_de_salida_al_obtener_proyecto(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response , SCHEMA_OUTPUT_GET_PROJECTS)

   

@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.performance
def test_014_validar_tiempo_de_respuesta_al_obtener_proyecto(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}    
      response = PlankaRequests.get(url,headers)
      log_request_response(url, response, headers)
      assert_response_time(response)
      
