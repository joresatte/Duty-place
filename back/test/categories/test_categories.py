from src.domain.setup import setup4, setup5
from src.domain.respuesta import Respuesta_3

def test_should_return_empty_list_categories():
    client= setup4()
    response = client.get("/api/categories")
    assert response.json == []

def test_should_return_list_of_categories():
    client= setup5()
    response = client.get("/api/categories")
    assert response.json == Respuesta_3