from src.domain.setup import setup8
from src.domain.respuesta import data_service, Respuesta_get_service

def test_return_category_services_posted():
    client= setup8()
    data= data_service
    response= client.post('/api/services/by-category', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/by-category')
    assert response.json== Respuesta_get_service