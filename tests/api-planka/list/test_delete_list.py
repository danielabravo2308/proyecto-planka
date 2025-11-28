
import pytest
from utils.constans import TOKEN_INVALID ,ID_LIST_NOT_EXISTS,ID_LIST_EMPTY,ID_LIST_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
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
          "test_025: eliminar_lista_con_token_valido",
          "test_026: eliminar_lista_con_token_invalido"
     ])

def test_eliminar_lista(get_token,use_fixture,token_value,expected_status,id_list):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_list_actual,expected_status",[
      pytest.param(ID_LIST_NOT_EXISTS,404,
                   id="test_027: eliminar_lista_con_id_lista_no_existente"),

      pytest.param(ID_LIST_EMPTY,404,
                   id="test_028: eliminar_lista_con_id_lista_vacia"),
      
      pytest.param(ID_LIST_INVALID_STRING,400,
                   id="test_029: eliminar_lista_con_id_lista_tipo_invalido")

   ])

def test_eliminar_lista_por_id_lista(get_token,id_list_actual,expected_status):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list_actual}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status == 404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)




