
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests


@pytest.mark.project_management
@pytest.mark.functional_positive
def test_013_eliminar_proyecto_con_token_valido(get_token,id_project):
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   AssertionStatusCode.assert_status_code_200(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
def test_014_eliminar_proyecto_con_token_invalido(id_project):
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   AssertionStatusCode.assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_project_invalid",[
         pytest.param("16329908991620567890453",
                  id=" eliminar proyecto con id proyecto no existente"),

         pytest.param("",
                  id="eliminar proyecto con id proyecto vacio"),

         pytest.param("abcsfdgfdgfdgdfgfdgdfg",
                  id="eliminar proyecto con id proyecto invalido valor cadena")
  ])

def test_015_eliminar_proyecto_por_id_proyecto_invalido(get_token,id_project_invalid):
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project_invalid}"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   AssertionStatusCode.assert_status_code_400_or_404(response)




