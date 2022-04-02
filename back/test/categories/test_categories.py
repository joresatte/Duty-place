from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.categories import CategoriesRepository, Categories

def test_should_return_empty_list_categories():
    Categories_Repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": Categories_Repository})
    client = app.test_client()

    response = client.get("/api/categories")
    assert response.json == []

def test_should_return_list_of_categories():
    categories_repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": categories_repository})
    client = app.test_client()

    category_1 = Categories(
        cat_id= "category_1",
        text= "Mudanzas",
        text_pictures= "text_pictures",
       
    )
    categories_repository.save(category_1)

    category_2 = Categories(
        cat_id= "category_2",
        text= "Limpiezas",
        text_pictures= "text_pictures",
    )
    categories_repository.save(category_2)
    
    response = client.get("/api/categories")
    assert response.json == [{
        "cat_id": "category_1",
        "text": "Mudanzas",
        "text_pictures": "text_pictures",
        
    },
    {
        "cat_id": "category_2",
        "text": "Limpiezas",
        "text_pictures": "text_pictures",
        
    },
    ]

