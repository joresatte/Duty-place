from src.domain.setup import setup10

def test_return_users_services_edited():
    client= setup10()
    data={
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vincen",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }
    response= client.put('/api/services/user_services/service_1/category_1', json= data)
    # assert response.status== 200
    response= client.get('/api/services/user_services')
    assert response.json== [
{
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vincen",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }
]