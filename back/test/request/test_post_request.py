from src.domain.setup import setupForPostedRequestData
from src.domain.respuesta import request_data

def test_return_post_request():
    client= setupForPostedRequestData()
    data= request_data
    response= client.post("/api/request", json= data)
    assert response.status== '200 OK'