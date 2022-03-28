from flask import Flask
from flask_cors import CORS
from src.domain.categories import Categories
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/categories", methods=["GET"])
    def get_all_categories():
        all_categories = repositories["categories"].get_all()
        return object_to_json(all_categories)

    @app.route("/api/services/by-category", methods=["GET"])
    def get_all_services_by_category():
        all_categories = repositories["categories_services"].get_all_services_by_category()
        return object_to_json(all_categories)

    @app.route("/api/services/by-category/<category_id>", methods=["GET"])
    def get_all_services_by_category_id(category_id):
        all_categories = repositories["categories_services"].get_category_services_by_cat_id(category_id)
        return object_to_json(all_categories)

    @app.route("/api/services/by-category/<id>", methods=["GET"])
    def get_all_services_by_category_id(category_id):
        all_categories = repositories["categories_services"].get_category_services_by_cat_id(category_id)
        return object_to_json(all_categories)

    # @app.route("/api/contact", methods=["POST"])
    # def contact_posted():
    #     user_id= request.headers.get("Authorization")
    #     body = request.json
    #     contact = Contact(**body)
    #     repositories["contact"].save(contact)
    #     return ''   
    
    # @app.route("/api/contact/<id>", methods=["GET"])
    # def get_contact_by_id(id):
    #     user_id= request.headers.get("Authorization")
    #     contact = repositories["contact"].get_by_id(id)
    #     if user_id == contact.user_id:
    #        return object_to_json(contact), 200
    #     else:
    #         return '', 403


    # @app.route("/api/contact/<id>", methods=["DELETE"])
    # def delete_contact_by_id(id):
    #     user_id= request.headers.get("Authorization")
    #     contact_removed = repositories["contact"].delete_contact_by_id(id)
    #     return ""

    # @app.route("/api/users", methods=["GET"])
    # def get_all_users():
    #     user_id= request.headers.get("Authorization")
    #     users = repositories["users"].get_all_users()
    #     return object_to_json(users)

    # @app.route("/api/contact/<id>", methods=["PUT"])
    # def modify_contact_by_id(id):
    #     user_id= request.headers.get("Authorization")
    #     data = request.json
    
    #     is_my_contact= user_id== data["user_id"]
    #     if not is_my_contact:
    #         return "", 403

    #     data['id']= id
    #     contact = Contact(
    #         id=data["id"],
    #         user_id=data["user_id"],
    #         first_name=data["first_name"],
    #         last_name=data["last_name"],
    #         email=data["email"],
    #         phone=data["phone"],

    #     )
    #     repositories["contact"].modify_contact_by_id(contact)
    #     return '', 200


    return app
