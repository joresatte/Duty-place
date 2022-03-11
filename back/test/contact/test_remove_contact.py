from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.contact import ContactRepository, Contact


def test_should_return_contact_deleted():
    contact_repository = ContactRepository(temp_file())
    app = create_app(repositories={"contact": contact_repository})
    client = app.test_client()
    josu = Contact(
        id= "contact-2",
        user_id= "josu_1",
        first_name= "Ibrahim ",
        last_name= "Diomande",
        email= "ibrahim@exemple.com",
        phone= "62654662657"
    )
    contact_repository.save(josu)

    request_delete_contact = client.delete("/api/contact/contact-2", 
    headers={'Authorization':'josu_1'})
    response = client.get("/api/contact")
    assert response.json == []
