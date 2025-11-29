# DIPLOMADO INGENIERIA DE CALIDAD DE SOFTWARE  COMERCIAL (3ra Edicion)

## TITULO : FRAMEWORK DE PRUEBAS AUTOMATIZADAS REST API DE LA APLICACION PLANKA


### Autor: Bravo Rueda Daniela

## Indice

- [Instalacion y Configuracion](#instalacion-y-configuracion)
- [Ejecucion de Pruebas](#ejecucion-de-pruebas)
- [Tipos de Pruebas](#tipos-de-pruebas)
- [Modulos Evaluados](#modulos-evaluados)
- [Reportes Allure](#reportes-allure)



# 1.Instalacion y Configuracion

1. Clonar el repositorio
```python
 git clone https://github.com/danielabravo2308/proyecto-planka.git
 cd PROYECTO-PLANKA
```
2. Crear y activar un entorno virtual
```python
  python -m venv env
```

3. Instalar Dependencias
```python
  pip install -r requirements.txt
```

4. Configuracion de variables de entorno
```python
  BASE_URI=http://localhost:3000/api
  USER_EMAIL=danielabravorueda@gmail.com
  USER_PASSWORD=db8826267
```
5. Ejecutar Servicios Docker para la aplicacion Planka
```python
 docker compose up -d
```
[⬆️ Volver al inicio](#indice)

# 2. Ejecucion de Pruebas

1. Ejecucion Completa de los casos de prueba
```python
pytest tests/   
```
2. Ejecucion completa detallada
```python
pytest -v  
```
[⬆️ Volver al inicio](#indice)

# 3. Ejecutar por tipo de pruebas
Para ejecutar casos de prueba por tipo de prueba realizada:

| Tipo de Pruebas            | Comando                          |
|-----------------------------|-----------------------------------|
| **Regresión**               | `pytest -m regresion`             |
| **Smoke**                       | `pytest -m smoke`                 |
| **Funcional Positivo**      | `pytest -m functional_positive`   |
| **Funcional Negativo**          | `pytest -m functional_negative`   |
| **Rendimiento**             | `pytest -m performance`           |
| **Partición de Equivalencia**   | `pytest -m equivalence_partition` |

[⬆️ Volver al inicio](#indice)

# 4. Ejecutar por modulo evaluados

Para ejecutar por modulo evaluado

| Modulo                    | Comando                          |
|---------------------------|----------------------------------|
| Gestion de Proyectos      | ` pytest .\project_management\`  |
| Tablero                   | ` pytest .\board\`               |
| Lista                     | ` pytest .\list\`                |
| Tarjeta                   | ` pytest .\card\`                |

[⬆️ Volver al inicio](#indice)

# 5. Generalizacion y Visualizacion de reportes

Para la generacion de reportes en Allure se sigue los siguientes pasos:

1. Generar Reporte
```python
pytest --alluredir=reports/allure-results 
```
2. Visualizar Reporte
```python
allure serve reports/allure-results
```
3. Reporte Allure HTML
```python
allure generate reports/allure-results --clean -o reports/allure-report-html
allure open reports/allure-report-html 
```
[⬆️ Volver al inicio](#indice)

