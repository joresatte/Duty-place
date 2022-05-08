from pyparsing import Regex
from flask import Flask, request
from flask_cors import CORS

from src.domain.category_services import  Category_services
from src.domain.users_services import  Services
from src.domain.regists import  Regists
from src.lib.utils import object_to_json
import re
import json

Regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
re_email= "[a-zA-Z0-9!#$%&'*_+-]([\.]?[a-zA-Z0-9!#$%&'*_+-])+@[a-zA-Z0-9]([^@&%$\/()=?¿!.,:;]|\d)+[a-zA-Z0-9][\.][a-zA-Z]{2,4}([\.][a-zA-Z]{2})?"
# def valid_email(email_addr: str):
#     # if re.match(re_email, email_addr.lower()):
#     #   return True
#     # else:
#     #    return False

def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world(): 
        return "...magic!"

    @app.route("/api/object_services", methods=["GET"])
    def get_object_services():
        obj_service= repositories["object_services"].get_all_object_services()
        return obj_service

    @app.route("/api/categories", methods=["GET"])
    def get_all_categories():
        all_categories = repositories["categories"].get_all()
        return object_to_json(all_categories)

    @app.route("/api/services/user_services", methods=["GET"])
    def get_all_users_services():
        all_services = repositories["services"].get_all_services()
        return object_to_json(all_services)

    @app.route("/api/services/user_services/<id>", methods=["GET"])
    def get_user_services_by_id(id):
        services = repositories["services"].get_user_services_by_id(id)
        return object_to_json(services)

    @app.route("/api/services/user_services", methods=["POST"])
    def post_user_services():
        data= request.json
        user_services = Services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
        )
        repositories["services"].save(user_services)
        return '', 200

    @app.route("/api/services/by-category", methods=["GET"])
    def get_all_services_by_category():
        all_categories = repositories["categories_services"].get_all_services_by_category()
        return object_to_json(all_categories)

    @app.route("/api/services/by-category/<category_id>", methods=["GET"])
    def get_all_services_by_category_id(category_id):
        all_categories = repositories["categories_services"].get_category_services_by_cat_id(category_id)
        return object_to_json(all_categories)

    @app.route("/api/services/by-category", methods=["POST"])
    def post_category_services():
        data= request.json
        services_by_category = Category_services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
        )
        repositories["categories_services"].save(services_by_category)
        return '', 200

    @app.route("/api/regists", methods=["POST"])
    def post_regists():
        data= request.json
        print("-------------", data)
        user= Regists(
            id= data['id'],
            email= data['email'],
            password= data['password']
            )
        print("-----------", user)
        if (data['id'])!= '' or (data['email'])!= '' or (data['password'])!= '':
            repositories["regists"].save(user)
            return '', 200
        else:
            return 'invalid regist', 403

    @app.route("/api/regists", methods=["GET"])
    def get_all_regists():
        all_regists = repositories["regists"].get_all_regists()
        return object_to_json(all_regists)

    @app.route("/api/regists/<id>", methods=["GET"])
    def get_regist_by_id(id):
        regist = repositories["regists"].get_regist_by_id(id)
        print('-----el registro:', regist)
        return regist.to_dict()

    @app.route("/api/login/Authenticated", methods=["POST"])
    def get_login():
        data= request.json
        # print("----aqui va el data:", data)
        user= repositories["regists"].get_by_email_and_password(data['email'], data ['password'])
        # print("------aqui va el user:", user)
        # print('----aqui va el user password:', data['password'])
        if user is None or (data['password']) != user.password or (data['email']) != user.email:
            return 'invalid log In', 401
        else:
            return object_to_json(user)
           


    # @app.route("/api/services/by-category/<id>", methods=["GET"])
    # def get_user_in_services_by_category_by_id(id):
    #     user_services = repositories["categories_services"].get_user_services_by_id(id)
    #     print(user_services)
    #     return object_to_json(user_services)

    # @app.route("/api/contact", methods=["POST"])
    # def contact_posted():
    #     user_id= request.headers.get("Authorization")
    #     data = request.json
    #     contact = Contact(**data)
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
