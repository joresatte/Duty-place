from src.domain.setup import setup1
from src.domain.respuesta import Respuesta_get_service

def test_should_return_services_list_by_category_id():
    client= setup1()
    
    response = client.get("/api/services/user_services/category_1")
    assert response.json == Respuesta_get_service
