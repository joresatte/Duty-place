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
            create table if not exists contacts (
                id varchar PRIMARY KEY,
                user_id varchar,
                first_name varchar,
                last_name varchar,
                phone varchar,
                email varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def search_by_user_id(self, user_id):
        sql = """select * from contacts where user_id=:user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'user_id': user_id})
        data = cursor.fetchall()
        contacts = []
        for item in data:
            contact = Contact(**item)
            contacts.append(contact)
        return contacts

    def get_by_id(self, id):
        sql = """SELECT * FROM contacts WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        data = cursor.fetchone()
        if data== None:
            contact= None
        else:
            contact = Contact(**data)
            
        return contact

    def deleted_contact_by_id(self, contact_deleted):
        sql = """ DELETE FROM contacts
            WHERE contact.id = :id """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": contact_deleted}
        )
        conn.commit()

    def modify_contact_by_id(self, modified_contact):

        sql = """ UPDATE contacts
            SET
            user_id= :user_id,
            first_name= :first_name,
            last_name= :last_name,
            email= :email,
            phone= :phone
            WHERE id= :id; """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, modified_contact.to_dict()
        )
        conn.commit()



    def save(self, contact):
        sql = """INSERT OR REPLACE into contacts (id, user_id, first_name, last_name, phone, email) values (
            :id, :user_id, :first_name, :last_name, :phone, :email
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            contact.to_dict(),
        )
        conn.commit()
