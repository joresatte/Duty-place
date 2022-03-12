import sys

sys.path.insert(0, "")

from src.domain.categories import CategoriesRepository, Categories

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