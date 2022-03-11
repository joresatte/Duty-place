from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.contact import ContactRepository, Contact

def test_should_save_contact():
    contact_repository = ContactRepository(temp_file())
    app = create_app(repositories={"contact": contact_repository})
    client = app.test_client()

    body= {
        "id": "contact-1",
        "user_id": "joseba_1",
        "first_name": "Jores",
        "last_name": "Vince",
        "email": "joresatte@exemple.com",
        "phone": "62654662656"
    }

    response = client.post("/api/contact", json=body)

    assert response.status_code == 200

    response_get = client.get("/api/contact/contact-1",
    headers={'Authorization':'joseba_1'})
    assert response_get.json == {
        "id": "contact-1",
        "user_id": "joseba_1",
        "first_name": "Jores",
        "last_name": "Vince",
        "full_name": "Jores Vince",
        "email": "joresatte@exemple.com",
        "phone": "62654662656"
    }
        
    

    
