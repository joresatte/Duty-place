from src.domain.setup import setup1
from src.domain.respuesta import Respuesta_1

def test_should_return_services_list():
    client= setup1()
   
    response = client.get("/api/services/user_services")
    assert response.json == Respuesta_1