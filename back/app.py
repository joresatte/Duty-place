from src.webserver import create_app
from src.domain.categories import CategoriesRepository
from src.domain.category_services import CategoryServicesRepository
from src.domain.users_services import ServicesRepository


database_path = "data/database.db"

repositories = {
    "categories": CategoriesRepository(database_path),
    "categories_services": CategoryServicesRepository(database_path),
    "services": ServicesRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
