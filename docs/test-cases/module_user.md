## 🧪 Casos de Prueba – Modulo Usuario

| ID | Titulo | Metodo | Prioridad | Entrada | Resultado esperado |
|----|-----------|-------|--------------|---------|--------------------|
| PLNK-001 | Crear usuario con datos requeridos | POST | ALTA    | "name": "sergio",<br>  "email": "sergio@test.com",<br>  "password": "8826267Sergy",<br>  "role": "admin"<br> | Status 200 |  
| PLNK-002 | No permitir crear usario con datos requeridos vacios |  POST | MEDIA    | "name": "",<br>  "email": "",<br>  "password": ""<br> | Status 400 |  
| PLNK-003 | Crear usuario con nombre de tipo valido | POST | BAJA   |   name = "Daniela"  | Status 200 |
| PLNK-004 | No permitir crear usuario con nombre de tipo de dato invalido  |  POST | BAJA     | name = <br> 123 , <br> "" | Status 400 |
| PLNK-005 | Crear usuario con email con formato valido |POST | BAJA  | email = daniela@test.com,  <br> sergio@test.com, <br> user.name@test.com, <br> user_name@test.com, <br> user+qa@test.com | Status 200 |
| PLNK-006 | No permitir crear usuario con un formato de email invalido | POST | MEDIA | email = <br> vacio ,<br> test.com , <br> test@ , <br> @test.com ,<br> dani @test.com, <br> dani@test| Status 400 |
| PLNK-007 | No permitir crear usuario con un email ya existente | POST | MEDIA | email = daniela@test.com | Status 400 |
| PLNK-008 | Crear usuario con un password con una longitud valida de caracteres | POST | MEDIA | password= <br>  >= 8 caracteres , <br> <= 256 caracteres , <br>  | Status 200 |
| PLNK-009 | No permitir crear usuario con un password de longitud invalida de caracteres | POST | MEDIA| password = <br> a , <br> "" , <br> 123 , <br> 257 caracteres | Status 400 |
| PLNK-010 | Crear usuario con un rol valido | POST | MEDIA | role = <br> admin , <br> projectOwner, <br> boardUser | Status 200 |
| PLNK-011 | No permitir crear un usuario con un rol no valido | POST | MEDIA | role = other , invite | Status 400 |
| PLNK-012 | Validar el esquema de tipo de datos del payload de entrada | POST | BAJA  |    | Status 200 |
| PLNK-013 | Validar el esquema de tipo de datos del payload de salida | POST | BAJA  |    | Status 200 |
| PLNK-014 | Validar el tiempo de respuesta sea menor a 2 segundos | POST | MEDIA |    | Status 200 |



