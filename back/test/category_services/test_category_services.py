from src.domain.setup import setup3, setup2
from src.domain.respuesta import response_user_service

def test_should_return_empty_services_list_by_category():
    client= setup3()
    response = client.get("/api/services/by-category")
    assert response.json == []

def test_should_return_services_list_by_category():
    client= setup2()
    
    response = client.get("/api/services/by-category")
    assert response.json== response_user_service
    