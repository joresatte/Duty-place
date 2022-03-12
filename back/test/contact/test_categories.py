from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.categories import CategoriesRepository, Categories

def test_should_return_empty_list_categories():
    Categories_Repository = CategoriesRepository(temp_file())
    app = create_app(repositories={"categories": Categories_Repository})
    client = app.test_client()

    response = client.get("/api/categories")
    assert response.json == []

# def test_should_return_list_of_contacts_by_user():
#     contact_repository = CategoriesRepository(temp_file())
#     app = create_app(repositories={"contact": contact_repository})
#     client = app.test_client()

#     joseba = Contact(
#         id= "contact-1",
#         user_id= "joseba_1",
#         first_name= "Jores",
#         last_name= "Vince",
#         email= "joresatte@exemple.com",
#         phone= "62654662656"
#     )
#     contact_repository.save(joseba)
#     josu = Contact(
#         id= "contact-2",
#         user_id= "josu_1",
#         first_name= "Ibrahim ",
#         last_name= "Diomande",
#         email= "ibrahim@exemple.com",
#         phone= "62654662657"
#     )
#     contact_repository.save(josu)
    
#     response = client.get("/api/contact", headers={
#         'Authorization':'joseba_1'
#         })
#     assert response.json == [{
#         "id": "contact-1",
#         "user_id": "joseba_1",
#         "first_name": "Jores",
#         "last_name": "Vince",
#         "full_name": "Jores Vince",
#         "email": "joresatte@exemple.com",
#         "phone": "62654662656"
#     },
#     ]

