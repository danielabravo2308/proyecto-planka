
import pytest
from utils.constans import TOKEN_INVALID , ID_PROJECT_INVALID_STRING,ID_PROJECT_NOT_EXISTS,ID_PROJECT_EMPTY 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests




@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.smoke
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "test_015: eliminar_proyecto_con_token_valido",
          "test_016: eliminar_proyecto_con_token_invalido"
          
     ])

def test_eliminar_proyecto(get_token,use_fixture,token_value,expected_status,id_project):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_project,expected_status",[
         pytest.param(ID_PROJECT_NOT_EXISTS,400,
                  id="test_017: eliminar_proyecto_con_id_proyecto_no_existente"),

         pytest.param(ID_PROJECT_EMPTY,404,
                  id="test_018: eliminar_proyecto_con_id_proyecto_vacio"),

         pytest.param(ID_PROJECT_INVALID_STRING,400,
                  id="test_019: eliminar_proyecto_con_id_proyecto_invalido_valor_cadena")
  ])

def test_eliminar_proyecto_por_id_proyecto(get_token,id_project,expected_status):
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status == 404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)




