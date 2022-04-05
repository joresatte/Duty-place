from src.domain.setup import setup6
from src.domain.respuesta import Respuesta_5

def test_should_return_regists_list():
    client= setup6()
    Body= Respuesta_5
    response = client.post("/api/regists", json= Body)
    assert response.status_code == 200