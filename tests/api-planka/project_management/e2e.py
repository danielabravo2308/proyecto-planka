
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE 
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests




@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_create_project(setup_add_project):
    url = EndpointPlanka.BASE_PROJECTS.value
    get_token , created_projects = setup_add_project
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())




@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_get_project(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)





@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.smoke
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
def test_delete_project(get_token,create_test_project):
    project_id = create_test_project
    ID_PROJECT = project_id
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.delete(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)



