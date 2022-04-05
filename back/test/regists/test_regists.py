from src.domain.setup import setup6, setup7
from src.domain.respuesta import Respuesta_4

def test_should_return_empty_regists_list():
    client= setup6()
    response = client.get("/api/regists")
    assert response.json == []

def test_should_return_regists_list():
    client= setup7()
    response = client.get("/api/regists")
    assert response.json == Respuesta_4