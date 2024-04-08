"""
    Test unitarios para cada función del main

    Prof. Tute Ávalos
"""
# pylint: disable=missing-function-docstring
import pytest
import main
from constantes import TABLAS

def test_abrir_conexion_existe():
    at_main = dir(main)
    assert 'abrir_conexion' in at_main

def test_consulta_generica():
    at_main = dir(main)
    assert 'consulta_generica' in at_main

@pytest.fixture
def conn_fixture():
    pytest.dbconn = main.abrir_conexion()

# El fixture se puede declarar pasando por parametro una variable
# con el mismo nombre del fixture ->
def test_abrir_conexion(conn_fixture):
    conn = pytest.dbconn
    assert conn

# O se puede declarar con el decorador @pytest.mark.usefixtures(<fixture>)
@pytest.mark.usefixtures("conn_fixture")
@pytest.mark.parametrize('tabla', TABLAS)
def test_chequear_tabla(tabla):
    resultado = main.consulta_generica(pytest.dbconn, f"SHOW TABLES LIKE '{tabla}'")
    assert len(resultado) == 1

def pytest_sessionfinish(session, status):
    # pylint: disable=unused-argument
    pytest.dbconn.close()
