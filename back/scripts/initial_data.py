import sys

sys.path.insert(0, "")

from src.domain.categories import CategoriesRepository, Categories
from src.domain.category_services import Categoryservicesepository, Category_services

database_path = "data/database.db"

category_1 = Categories(
        cat_id= "category_1",
        text= "Mudanzas",
       
    )
category_2 = Categories(
    cat_id= "category_2",
    text= "Limpiezas",
    
)
category_3 = Categories(
        cat_id= "category_3",
        text= "Cuidados",
       
    )
category_4 = Categories(
        cat_id= "category_4",
        text= "Mantenimientos",
       
    )
contact_repository = CategoriesRepository(database_path)
contact_repository.save(category_1)
contact_repository.save(category_2)
contact_repository.save(category_3)
contact_repository.save(category_4)

services_repository = Categoryservicesepository(database_path)
services_repository.save(
    Category_services(
        id= "service_1",
        cat_id= "category_1",
        user_name= "vince",
        text= "Mudanzas",
        phone= "024-639-2574",
        email= "reinabo@vince.com",
        city= "Bilbao",
    )
)
services_repository.save(
    Category_services(
        id= "service_23",
        cat_id= "category_1",
        user_name= "oouygj",
        text= "Mudanzas",
        phone= "024-639-2574",
        email= "aqsdo@voiuce.com",
        city= "xdghbao",
    )
)
services_repository.save(
    Category_services(
        id= "service_12",
        cat_id= "category_1",
        user_name= "rfedbj",
        text= "Mudanzas",
        phone= "024-768-26544",
        email= "vhjbo@dsadce.com",
        city= "erhjkj",
    )
)

services_repository.save(
    Category_services(
        id= "service_9",
        cat_id= "category_2",
        user_name= "oshulem0",
        text= "Limpiezas",
        phone= "424-639-9574",
        email= "fbadland0@bizjournals.com",
        city= "Tayirove",
    )
)
services_repository.save(
    Category_services(
        id= "service_74",
        cat_id= "category_2",
        user_name= "teerarem0",
        text= "Limpiezas",
        phone= "124-234-9574",
        email= "efmland0@bizjournals.com",
        city= "sdjnkjrove",
    )
)
services_repository.save(
    Category_services(
        id= "service_45",
        cat_id= "category_2",
        user_name= "oshhgkhhj",
        text= "Limpiezas",
        phone= "008-639-94374",
        email= "jnk@bizjouals.com",
        city= "nkmncfe",
    )
)

services_repository.save(
    Category_services(
        id= "service_97",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        phone= "810-629-1584",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)
services_repository.save(
    Category_services(
        id= "service_80",
        cat_id= "category_3",
        user_name= "eewols3",
        text= "Cuidados",
        phone= "481-201-6380",
        email= "ecardoo3@wufoo.com",
        city= "Tanahmerah",
    )
)
services_repository.save(
    Category_services(
        id= "service_71",
        cat_id= "category_3",
        user_name= "Roanne",
        text= "Cuidados",
        phone= "382-214-1560",
        email= "msisson2@disqus.com",
        city= "awaldron2",
    )
)

services_repository.save(
    Category_services(
        id= "service_32",
        cat_id= "category_4",
        user_name= "rnisen5",
        text= "Mantenimientos",
        phone= "562-575-0936",
        email= "dillsley5@shareasale.com",
        city= "Olival Basto",
    )
)
services_repository.save(
    Category_services(
        id= "service_56",
        cat_id= "category_4",
        user_name= "mdowle6",
        text= "Mantenimientos",
        phone= "939-267-4173",
        email= "kreisen6@earthlink.net",
        city= "Tubli",
    )
)
services_repository.save(
    Category_services(
        id= "service_64",
        cat_id= "category_4",
        user_name= "atunniclisse7",
        text= "Mantenimientos",
        phone= "843-625-9927",
        email= "grickerd7@dion.ne.jp",
        city= "Zielona Góra",
    )
)
