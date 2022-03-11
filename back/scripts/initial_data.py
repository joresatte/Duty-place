import sys
from unicodedata import name

sys.path.insert(0, "")


from src.domain.info import InfoRepository, Info
from src.domain.contact import ContactRepository, Contact
from src.domain.users import UserRepository, User

database_path = "data/database.db"

info_repository = InfoRepository(database_path)
info_repository.save(Info(app_name="contact-list"))

user_repository = UserRepository(database_path)
user_repository.save(
   User( 
        id= "user-1",
        name= "joseba"
    )
)
user_repository.save(
    User(
        id= "user-2",
        name= "josu"
    )
)

joseba = Contact(
    id= "contact-1",
    user_id= "user-1",
    first_name= "Jores",
    last_name= "Vince",
    email= "joresatte@exemple.com",
    phone= "62654662656"
)
josu = Contact(
    id= "contact-2",
    user_id= "user-2",
    first_name= "Ibrahim",
    last_name= "Diomande",
    email= "ibrahim@exemple.com",
    phone= "62654662657"
)
contact_repository = ContactRepository(database_path)
contact_repository.save(joseba)
contact_repository.save(josu)