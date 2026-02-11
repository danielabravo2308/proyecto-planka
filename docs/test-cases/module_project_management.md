# 🧪 Casos de Prueba – Modulo Project Management

| ID | Titulo | Metodo | Prioridad | Entrada | Resultado esperado |
|----|-----------|-------|--------------|---------|--------------------|
| PLNK-001 | Crear proyecto con token valido | POST | ALTA    |     | Status 200 | 
| PLNK-002 | Crear proyecto con token invalido | POST | ALTA    |     | Status 401 | 
| PLNK-003 | Validar el payload de salida al crear nuevo proyecto | POST | MEDIA    |     | Status 200 | 
| PLNK-004 | Validar el payload de entrada al crear nuevo proyecto | POST | MEDIA    |     | Status 200 | 
| PLNK-005 | No permitir crear proyecto al ingresar en el campo type un valor invalido | POST | MEDIA   | type = <br> "" , <br> "other"     | Status 400 | 
| PLNK-006 | Crear proyecto al ingresar en el campo type un valor valido | POST | MEDIA   | type = <br> "shared" , <br> "private"     | Status 200 | 
| PLNK-007 | No permitir crear proyecto al ingresar en el campo name un valor invalido | POST | MEDIA   | name = <br> "" , <br> 1234     | Status 400 | 
| PLNK-008 | Crear proyecto al ingresar en el campo name un valor valido | POST | MEDIA   | name = <br> "Nuevo Proyecto"    | Status 200 | 
| PLNK-009 | Obtener proyecto con token valido | GET | ALTA   |    | Status 200 | 
| PLNK-010 | No permitir obtener proyecto con token invalido | GET | ALTA   |    | Status 401 | 
| PLNK-011 | Validar el payload de salida al obtener proyecto | GET | MEDIA   |    | Status 200 | 
| PLNK-012 | Validar el tiempo de respuesta al obtener proyectos | GET | MEDIA   |    | Status 200 | 
| PLNK-013 | Eliminar proyecto con token valido | DELETE | ALTA   |    | Status 200 |
| PLNK-014 | No permitir eliminar proyecto con token invalido | DELETE | ALTA   |    | Status 401 |  
| PLNK-015 | No permitir eliminar proyecto con id de proyecto invalido| DELETE | ALTA   | id=  <br>  id_no_exists, <br> "",<br> id_string   | Status 400 o 404 |  