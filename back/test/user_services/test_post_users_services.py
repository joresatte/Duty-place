from src.domain.setup import setup7
from src.domain.respuesta import response_get_service, data_service

def test_return_users_services_posted():
    client= setup7()
    data= data_service
    response= client.post('/api/services/user_services', json= data)
    assert response.status== '200 OK'
    response= client.get('/api/services/user_services')
    assert response.json== response_get_service