from src.domain.setup import setup1
from src.domain.respuesta import Respuesta_13

def test_should_return_one_user_services_by_id():
    client= setup1()
   
    response = client.delete("/api/services/user_services/service_1/category_1")
    assert response.status == '200 OK'
    response= client.get("/api/services/user_services")
    assert response.json == Respuesta_13
    
