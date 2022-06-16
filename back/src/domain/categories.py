import sqlite3

class Categories:
    def __init__(self, cat_id, text, text_pictures):
        self.cat_id = cat_id
        self.text = text
        self.text_pictures = text_pictures

    def to_dict(self):
        return {
            "cat_id": self.cat_id,
            "text": self.text,
            "text_pictures": self.text_pictures,
        }


class CategoriesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def drop_tables(self):
        sql = """
            DROP TABLE IF EXISTS categories
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def init_tables(self):
        sql = """
            create table if not exists categories (
                cat_id varchar primary key,
                text varchar,
                text_pictures varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from categories"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [Categories(**item) for item in data]
        return users

    def get_by_id(self, cat_id):
        sql = """SELECT * FROM users WHERE cat_id=: cat_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"cat_id": cat_id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Categories(**data)

        return user

    def save(self, category):
        sql = """insert into categories (cat_id, text,text_pictures) values (
            :cat_id, :text, :text_pictures
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"cat_id": category.cat_id, "text": category.text, "text_pictures": category.text_pictures}
        )
        conn.commit()



