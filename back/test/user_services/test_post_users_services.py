from src.domain.setup import setup7
from src.domain.respuesta import Respuesta_2

def test_return_users_services_posted():
    client= setup7()
    data= Respuesta_2
    response= client.post('/api/services/user_services', json= data)
    assert response.status== '200 OK'
    response= client.get('/api/services/user_services')
    assert response.json== Respuesta_2