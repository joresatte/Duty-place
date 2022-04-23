from src.domain.setup import setup8
from src.domain.respuesta import Respuesta_2

def test_return_category_services_posted():
    client= setup8()
    data= Respuesta_2
    response= client.post('/api/services/by-category', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/by-category')
    assert response.json== Respuesta_2