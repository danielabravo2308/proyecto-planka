import os
from src.routes.request import PlankaRequests



def generate_token():
    BASE_URI = os.getenv("BASE_URI")
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")

    if not BASE_URI or not USER_EMAIL or not USER_PASSWORD:
        raise RuntimeError("Variables de entorno no definidas")


    url = f"{BASE_URI}/access-tokens"
    payload = {
            "emailOrUsername": USER_EMAIL,
            "password": USER_PASSWORD
    }
    headers = {'Content-Type': 'application/json'}
    response = PlankaRequests.post(url, headers, payload)
    response_json = response.json()
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    access_token = response_json['item']
    return access_token


if __name__ == "__main__":
    token = generate_token()
    if token:
        print("Token generado:", token)
    else:
        print("No se pudo generar el token")
