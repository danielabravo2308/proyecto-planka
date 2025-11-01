from faker import Faker
import random

fake = Faker("es_ES")   # puedes cambiar locale, p.ej. "en_US"
ROLES = ["admin", "user", "editor", "viewer"]
def generate_faker_user_payload():
    return {
        "name": fake.name(),                        # nombre completo aleatorio
        "email": fake.unique.email(),               # email único
        "password": fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        ),                                          # password que cumple complejidad
        "role": random.choice(ROLES)                # rol aleatorio de la lista
    }


