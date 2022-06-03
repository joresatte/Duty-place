from src.domain.setup import setup10
from src.domain.respuesta import updater, updated

def test_return_users_services_edited():
    client= setup10()
    data= updater
    response= client.put('/api/services/user_services/service_1/category_1/Mudanzas', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/user_services/service_1')
    assert response.json== updated