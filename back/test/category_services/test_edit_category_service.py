from src.domain.setup import setup9
from src.domain.respuesta import Respuesta_15, Respuesta_14

def test_return_category_services_edited():
    client= setup9()
    data= Respuesta_15
    response= client.put('/api/services/by-category/service_1/category_1/Mudanzas', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/by-category/category_1')
    assert response.json== Respuesta_14