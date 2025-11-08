
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.routes.request import PlankaRequests
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE 
from utils.logger_helper import get_logger


logger = get_logger("board_fixture")

@pytest.fixture(scope="function")
def post_test_board(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = PAYLOAD_BOARD_CREATE
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}',}
    response = PlankaRequests.post(url,headers,payload)
    data = response.json()
    board_id = data["item"]["id"]
    yield board_id
   
   

@pytest.fixture(scope="module")
def setup_add_board(get_token):
    created_boards = []
    logger.info("Setup iniciado para creación de tableros")
    yield get_token,created_boards

    logger.info("Iniciando teardown de tableros creados")
    for board in created_boards:
        board_id = board.get("item", {}).get("id")
        try:
              delete_url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{board_id}"
              headers = {'Authorization': f'Bearer {get_token}'} 
              delete_response = PlankaRequests.delete(delete_url,headers=headers)
              if AssertionStatusCode.assert_status_code_200(delete_response) == 200:
                    logger.info(f"Tablero eliminado correctamente: {board_id}")
              else:
                   logger.error(f" No se pudo eliminar el tablero {board_id}. ")
        except Exception as e:
          logger.exception(f"Error eliminando tablero: {e}")