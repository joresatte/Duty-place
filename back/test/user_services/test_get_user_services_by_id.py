from src.domain.setup import setup1
from src.domain.respuesta import data_service, Respuesta_get_service

def test_should_return_one_user_services_by_id():
    client= setup1()
   
    response = client.get("/api/services/user_services/service_1")
    assert response.json == Respuesta_get_service

def test_should_return_one_user_services_by_id_cat_id_text():
    client= setup1()
   
    response = client.get("/api/services/user_services/service_1/category_1/Mudanzas")
    assert response.json == data_service
    
