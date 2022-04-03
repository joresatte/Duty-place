from src.domain.setup import setup2
from src.domain.respuesta import Respuesta_2

def test_should_return_services_list_by_category_id():
    client= setup2()
    
    response = client.get("/api/services/by-category/category_1")
    assert response.json == Respuesta_2
