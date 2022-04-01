import sqlite3

class Category_services:
    def __init__(self, id, cat_id, user_name, text, intro, price, text_pictures, textarea, email, phone, city):
        self.id= id
        self.cat_id= cat_id
        self.user_name= user_name
        self.text= text
        self.intro= intro
        self.price= price
        self.text_pictures= text_pictures
        self.textarea= textarea
        self.email= email
        self.phone= phone
        self.city= city

    def to_dict(self):
        return {
           "id": self.id,
            "cat_id": self.cat_id,
            "user_name": self.user_name,
            "text": self.text,
            "intro": self.intro,
            "price": self.price,
            "text_pictures": self.text_pictures,
            "textarea": self.textarea,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,
        }

class CategoryServicesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists categories_services (
               id varchar,
                cat_id varchar,
                user_name varchar,
                text varchar,
                intro varchar,
                price varchar,
                text_pictures varchar,
                textarea varchar,
                phone varchar,
                email varchar,
                city varchar  
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_services_by_category(self):
        sql = """select * from categories_services"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        services = []
        for item in data:
            each_category_service = Category_services(
                 id= item["id"],
                cat_id= item["cat_id"],
                user_name= item["user_name"],
                text= item["text"],
                intro= item["intro"],
                price= item["price"],
                text_pictures= item["text_pictures"],
                textarea= item['textarea'],
                phone= item["phone"],
                email= item["email"],
                city= item["city"],
            )
            services.append(each_category_service)
        return services

    def get_category_services_by_cat_id(self, category_id):
        sql = """SELECT * FROM categories_services WHERE cat_id= :cat_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"cat_id": category_id})
        data = cursor.fetchall()
        services = []
        for item in data:
            services_by_category_id = Category_services(
                 id= item["id"],
                cat_id= item["cat_id"],
                user_name= item["user_name"],
                text= item["text"],
                intro= item["intro"],
                price= item["price"],
                text_pictures= item["text_pictures"],
                textarea= item['textarea'],
                phone= item["phone"],
                email= item["email"],
                city= item["city"],
            )
            services.append(services_by_category_id)
        return services

    def save(self, user_service):
        sql = """INSERT into categories_services (id, cat_id, user_name, text, intro, price, text_pictures, textarea, phone, email, city) values (
            :id, :cat_id, :user_name, :text, :intro, :price, :text_pictures, :textarea, :phone, :email, :city
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            user_service.to_dict(),
        )
        conn.commit()
