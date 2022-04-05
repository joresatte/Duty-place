from src.domain.setup import setup6
from src.domain.respuesta import Respuesta_6, Respuesta_7, Respuesta_8

def test_should_validate_user():
    client= setup6()
    Body= Respuesta_6
    response = client.post("/api/login/Authenticated", json= Body)
    assert response.status_code == 200
    assert response.json== Respuesta_7

def test_should_invalidate_user():
    client= setup6()
    Body= Respuesta_8
    response = client.post("/api/login/Authenticated", json= Body)
    assert response.status_code == 401

