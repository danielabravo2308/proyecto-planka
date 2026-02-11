import pytest
from src.assertions.assertion_general import assert_response_time
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.user_payloads import PAYLOAD_USER_CREATE_EMPTY,PAYLOAD_USER_CREATE
from src.resources.schemas.user_schema import SCHEMA_USER_CREATE_INPUT , SCHEMA_USER_CREATE_OUTPUT
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests

@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.parametrize("name, email, password, role", [
    ("danielab","dani2308@gmail.com","dani2308","admin"),
    ("mariela","mariel123@gmail.com","dmari1234","admin"),
    ("diego","diegote2525@gmail.com","diego1234","admin")
])
def test_001_crear_usuario_con_datos_requeridos(get_token , name , email , password , role ):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    payload = {"name": name,"email": email,"password": password,"role": role}
    headers = {
    'Authorization': f'Bearer {get_token}',
    'Content-Type': 'application/json'
    }

    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_200(response)


@pytest.mark.functional_negative
def test_002_crear_usuario_con_datos_requeridos_vacios(get_token):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = {
    'Authorization': f'Bearer {get_token}',
    'Content-Type': 'application/json'
    }
    response = PlankaRequests.post(url,headers,payload=PAYLOAD_USER_CREATE_EMPTY)
    log_request_response(url, response, headers, payload=PAYLOAD_USER_CREATE_EMPTY)
    AssertionStatusCode.assert_status_code_400(response)


@pytest.mark.smoke
@pytest.mark.functional_positive

def test_003_crear_usuario_con_el_campo_nombre_de_tipo_valido(get_token):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = {
    'Authorization': f'Bearer {get_token}',
    'Content-Type': 'application/json'
    }
    response = PlankaRequests.post(url,headers,payload=PAYLOAD_USER_CREATE)
    log_request_response(url, response, headers, payload=PAYLOAD_USER_CREATE)
    AssertionStatusCode.assert_status_code_200(response)



@pytest.mark.functional_negative
@pytest.mark.parametrize("name, email, password, role", [
    (1234, "dani2308@gmail.com", "dani2308", "admin"),
    ("", "mariela123@gmail.com", 123456789, "admin")
],
ids=["Campo name con tipo de dato numérico", 
     "Campo name vacío "
    ])
#@pytest.mark.xfail(reason=" El sistema permite crear usuario al ingresar un tipo de dato invalido en el campo nombre" , run=True)
def test_004_crear_usuario_con_el_campo_nombre_de_tipo_invalido(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    payload = {"name": name,"email": email,"password": password,"role": role}
    headers = {'Authorization': f'Bearer {get_token}',
               'Content-Type': 'application/json'
    }
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.parametrize("name, email, password, role", [
    ("danielab", "daniela@test.com", "dani2308", "admin"),
    ("sergi", "sergio@test.com", "sergio1234", "admin"),
    ("user", "user.name@test.com", "user1234", "admin"),
    ("name2308", "user_name@test.com", "name2308", "admin"),
    ("qauser", "user+qa@test.com", "userqai1234", "admin") 
])
  
def test_005_crear_usuario_con_el_campo_email_con_formato_valido(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_200(response)



@pytest.mark.functional_negative
@pytest.mark.parametrize("name, email, password, role", [
    ("danielab", "", "dani2308", "admin"),
    ("sergi", "test.com", "sergio1234", "admin"),
    ("user", "user.name@", "user1234", "admin"),
    ("name2308", "@test.com", "name2308", "admin"),
    ("qauser", "user qa@test.com", "userqai1234", "admin"),
    ("dani", "dani@test", "userqai1234", "admin")

],
ids=[
    "Campo email vacío",
    "Campo email sin el símbolo @",
    "Campo email sin el dominio",
    "Campo email sin el nombre de usuario",
    "Campo email con espacios",
    "Campo email con dominio incompleto"
])
def test_006_crear_usuario_con_el_campo_email_con_formato_invalido(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_400(response)


@pytest.mark.functional_negative
@pytest.mark.parametrize("name, email, password, role", [
    ("danielabravo", "daniela2309@gmail.com", "dani2308", "admin"),
    ("daniela", "daniela2309@gmail.com", "dani2308", "admin")
],
ids=[
    "email de usuario creado previamente",
    "email usado nuevamente para crear otro usuario"
])
def test_007_crear_usuario_con_email_ya_existente(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_409(response)



@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.parametrize("name, email, password, role", [
    ("daniela", "daniela@test.com", "12345678", "admin"), 
    ("sergio", "sergio@test.com", "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345", "admin") 
],
ids=[
    "password con longitud mínima permitida de 8 caracteres",
    "password con longitud máxima permitida de 255 caracteres"
])
def test_008_crear_usuario_con_password_con_longitud_valida(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }   
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_200(response)


@pytest.mark.functional_negative
@pytest.mark.parametrize("name, email, password, role", [
    ("daniela", "daniela@test.com", "abc", "admin"),
    ("sergio", "sergio@test.com", "", "admin"),
    ("name2308", "user_name@test.com", "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456", "admin")
],
ids=[
    "password con longitud menor a la mínima permitida",
    "password vacía",
    "password con longitud mayor a la máxima permitida"
])
def test_009_crear_usuario_con_password_con_longitud_invalida(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }   
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_400(response)


@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.parametrize("name, email, password, role", [
    ("daniel", "daniel@test.com", "dani2308", "admin"),
    ("sergi", "sergio@test.com", "sergio1234", "projectOwner"),
    ("user", "user.name@test.com", "user1234", "boardUser")
],
ids=[
    "Crear usuario con rol admin",
    "Crear usuario con rol projectOwner",
    "Crear usuario con rol boardUser"
])
def test_010_crear_usuario_con_el_campo_rol_valido(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }   
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload) 
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_200(response)


@pytest.mark.functional_negative
@pytest.mark.parametrize("name, email, password, role", [
    ("daniel", "daniel@test.com", "dani2308", "other"),
    ("sergi", "sergio@test.com", "sergio1234", "invited"),
],
ids=[
    "Crear usuario con rol inválido other",
    "Crear usuario con rol inválido invited"
])
def test_011_crear_usuario_con_el_campo_rol_invalido(get_token,name,email,password,role):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    payload = {"name": name,"email": email,"password": password,"role": role}
    response = PlankaRequests.post(url,headers,payload=payload)
    log_request_response(url, response, headers, payload=payload)
    AssertionStatusCode.assert_status_code_400(response)


@pytest.mark.smoke
@pytest.mark.functional_positive
def test_012_validar_esquema_de_tipo_de_datos_del_payload_de_entrada(get_token):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }

    response = PlankaRequests.post(url,headers,payload=PAYLOAD_USER_CREATE)
    log_request_response(url, response, headers, payload=PAYLOAD_USER_CREATE, schema=SCHEMA_USER_CREATE_INPUT)
    AssertionSchemas.validate_schema_input_payload(PAYLOAD_USER_CREATE, SCHEMA_USER_CREATE_INPUT)

   

@pytest.mark.smoke
@pytest.mark.functional_positive
def test_013_validar_esquema_de_tipo_de_datos_del_payload_de_salida(get_token):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    response = PlankaRequests.post(url,headers,payload=PAYLOAD_USER_CREATE)
    log_request_response(url, response, headers, payload=PAYLOAD_USER_CREATE, schema=SCHEMA_USER_CREATE_OUTPUT)
    AssertionSchemas.validate_schema_output_payload(response, SCHEMA_USER_CREATE_OUTPUT)
    

@pytest.mark.smoke
@pytest.mark.performance
def test_014_validar_el_tiempo_de_respuesta_al_crear_un_usuario(get_token):
    url = EndpointPlanka.BASE_USER_MAJOR.value
    headers = { 'Authorization': f'Bearer {get_token}',
                'Content-Type': 'application/json'
    }
    response = PlankaRequests.post(url,headers,payload=PAYLOAD_USER_CREATE)
    log_request_response(url, response, headers, payload=PAYLOAD_USER_CREATE)
    assert_response_time(response)