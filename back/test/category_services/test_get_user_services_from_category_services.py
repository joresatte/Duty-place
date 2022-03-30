from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.category_services import CategoryServicesRepository, Category_services

def test_should_return_services_list_by_category_id():
    services_repository = CategoryServicesRepository(temp_file())
    app = create_app(repositories={"services": services_repository})
    client = app.test_client()

    user_1= Category_services(
       id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
    services_repository.save(user_1)
    
    user_2= Category_services(
        id= "service_2",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
    user_3= Category_services(
        id= "service_50",
        cat_id= "category_2",
        user_name= "zegerton1",
        text= "Limpiezas",
        phone= "382-214-1560",
        email= "wglenister1@latimes.com",
        city= "Al Burayqah",
    )
    services_repository.save(user_2)
    services_repository.save(user_3)
    
    response = client.get("/api/services/user_services/service_1")
    assert response.json == [{
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    },
    {
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    },
    {
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    }
    ]
    
