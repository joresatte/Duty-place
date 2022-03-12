from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.category_services import Categoryservicesepository, Category_services

def test_should_return_empty_services_list_by_category():
    services_Repository = Categoryservicesepository(temp_file())
    app = create_app(repositories={"categories_services": services_Repository})
    client = app.test_client()

    response = client.get("/api/services/by-category")
    assert response.json == []

def test_should_return_services_list_by_category():
    services_repository = Categoryservicesepository(temp_file())
    app = create_app(repositories={"categories_services": services_repository})
    client = app.test_client()

    user_1= Category_services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao"
    )
    services_repository.save(user_1)

    user_2= Category_services(
        id= "service_2",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove"
    )
    services_repository.save(user_2)
    
    response = client.get("/api/services/by-category")
    assert response.json == [{
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao"
        
    },
    {
        "id": "service_2",
        "cat_id": "category_2",
        "user_name": "oshulem0",
        "text": "Limpiezas",
        "phone": "424-639-9574",
        "email": "fbadland0@bizjournals.com",
        "city": "Tayirove"
        
    },
    ]

