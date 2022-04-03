from src.domain.setup import setup2
def test_should_return_services_list_by_category_id():
    client= setup2()
    
    response = client.get("/api/services/by-category/category_1")
    assert response.json == [{
         "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas",
        "price": "por 7$ la hora",
        "text_pictures": "foto",
        "textarea": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    }
    ]
    
