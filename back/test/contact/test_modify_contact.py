from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.contact import ContactRepository, Contact


def test_should_return_contact_deleted():
    contact_repository = ContactRepository(temp_file())
    app = create_app(repositories={"contact": contact_repository})
    client = app.test_client()
    old_contact_josu = Contact(
        id= "contact-2",
        user_id= "josu_1",
        first_name= "Ibrahim ",
        last_name= "Diomande",
        email= "ibrahim@exemple.com",
        phone= "62654662657"
    )
    contact_repository.save(old_contact_josu)

    new_contact_josu = Contact(
        id= "contact-2",
        user_id= "josu_1",
        first_name= "Diomande",
        last_name= "Ibrahim",
        email= "ibrahim@exemple.com",
        phone= "72654662457"
    )
    contact_repository.modify_contact_by_id(new_contact_josu)

    request_modify_contact = client.get("/api/contact/contact-2",
    headers={'Authorization':'josu_1'})
    #response = client.get("/api/contact")
    assert request_modify_contact.json ==(
        {"id": "contact-2",
        "user_id": "josu_1",
        "first_name": "Diomande",
        "last_name": "Ibrahim",
        "full_name": "Diomande Ibrahim",
        "email": "ibrahim@exemple.com",
        "phone": "72654662457"}
    )
