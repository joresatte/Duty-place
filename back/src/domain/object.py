import sqlite3

class Object:
    def __init__(self, cat_id, user_name, text, intro, price, text_pictures, textarea, email, phone, city):
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


class ObjectServicesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def drop_tables(self):
        sql = """
            DROP TABLE IF EXISTS objectservices
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def init_tables(self):
        sql = """
            create table if not exists objectservices (
                cat_id varchar primary key,
                user_name varchar,
                text_pictures varchar,
                text varchar,
                intro varchar,
                price varchar,
                textarea varchar,
                email varchar,
                phone varchar,
                city varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from objectservices"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [Object(**item) for item in data]
        return users
