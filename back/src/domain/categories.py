import sqlite3

class Categories:
    def __init__(self, cat_id, text):
        self.cat_id= cat_id
        self.text = text

    def to_dict(self):
        return {
            "cat_id": self.cat_id,
            "text": self.text,
        }

class CategoriesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists categories (
                cat_id varchar,
                text varchar
                
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    # def search_by_user_id(self, cat_id):
    #     sql = """select * from categories where cat_id= :cat_id"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql, {'cat_id': cat_id})
    #     data = cursor.fetchall()
    #     categories = []
    #     for item in data:
    #         category = Categories(**item)
    #         categories.append(category)
    #     return categories
    
    def get_all(self):
        sql = """select * from categories"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        categories = []
        for item in data:
            each_category = Categories(
                cat_id= item["cat_id"],
                text= item["text"],
            )
            categories.append(each_category)
        return categories

    def get_by_cat_id(self, cat_id):
        sql = """SELECT * FROM categories WHERE cat_id= :cat_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"cat_id": cat_id})
        data = cursor.fetchone()
        if data== None:
            category= None
        else:
            category = Categories(**data)
        return category

    # def deleted_contact_by_id(self, contact_deleted):
    #     sql = """ DELETE FROM categories
    #         WHERE contact.id = :id """
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         sql, {"id": contact_deleted}
    #     )
    #     conn.commit()

    # def modify_contact_by_id(self, modified_contact):

    #     sql = """ UPDATE categories
    #         SET
    #         user_id= :user_id,
    #         first_name= :first_name,
    #         last_name= :last_name,
    #         email= :email,
    #         phone= :phone
    #         WHERE id= :id; """
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         sql, modified_contact.to_dict()
    #     )
    #     conn.commit()



    def save(self, contact):
        sql = """INSERT OR REPLACE into categories (cat_id, text) values (
            :cat_id, :text
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            contact.to_dict(),
        )
        conn.commit()
