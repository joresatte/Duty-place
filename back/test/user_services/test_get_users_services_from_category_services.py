from src.domain.setup import setup1
from src.domain.respuesta import response_user_service

def test_should_return_services_list():
    client= setup1()
   
    response = client.get("/api/services/user_services")
    assert response.json == response_user_service