import pytest
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import get_logger

logger = get_logger("project_fixture")


@pytest.fixture(scope="function")
def create_test_project(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
      response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
      data = response.json()
      project_id = data["item"]["id"]
      yield project_id
   
      

  
@pytest.fixture(scope="module")
def setup_add_project(get_token):
    created_projects = []
    logger.info("Setup iniciado para creación de proyectos")
    yield get_token,created_projects

    logger.info("Iniciando teardown de proyectos creados")
    for project in created_projects:
        project_id = project.get("item", {}).get("id")
        try:
              delete_url = f"{EndpointPlanka.BASE_PROJECTS.value}/{project_id}"
              headers = {'Authorization': f'Bearer {get_token}'} 
              delete_response = PlankaRequests.delete(delete_url,headers=headers)
              if AssertionStatusCode.assert_status_code_200(delete_response) == 200:
                    logger.info(f"Proyecto eliminado correctamente: {project_id}")
              else:
                   logger.error(f" No se pudo eliminar el proyecto {project_id}. ")
        except Exception as e:
          logger.exception(f"Error eliminando proyecto: {e}")           
    

    