from src.domain.setup import setup1
from src.domain.respuesta import Respuesta_2

def test_should_return_one_user_services_by_id():
    client= setup1()
   
    response = client.get("/api/services/user_services/service_1")
    assert response.json == Respuesta_2
    
