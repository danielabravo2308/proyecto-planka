
import pytest
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from utils.logger_helper import get_logger


logger = get_logger("card_fixture")

@pytest.fixture(scope="function")
def post_card(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = PAYLOAD_CREATE_CARD
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url, headers, payload)
    data = response.json()
    card_id = data["item"]["id"]
    yield card_id
   

@pytest.fixture(scope="module")
def setup_add_card(get_token):
    created_cards = []      
    logger.info("Setup iniciado para creación de tarjetas")
    yield get_token,created_cards


    logger.info("Iniciando teardown de tarjetas creados")
    for card in created_cards:
        card_id = card.get("item", {}).get("id")
        try:
            delete_url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{card_id}"
            headers = {'Authorization': f'Bearer {get_token}'} 
            delete_response = PlankaRequests.delete(delete_url,headers)
            if delete_response.status_code == 200:
                     logger.info(f"Tarjeta eliminado correctamente: {card_id}")
            else:
                    logger.error(f" No se pudo eliminar el tarjeta {card_id}. ")
        except Exception as e:
            logger.exception(f"Error eliminando tarjeta: {e}")  