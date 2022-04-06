import email
import sqlite3

class Regists:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class RegistsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def drop_tables(self):
        sql = """
            DROP TABLE IF EXISTS registros
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def init_tables(self):
        sql = """
            create table if not exists registros (
                id varchar,
                email varchar,
                password varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_regists(self):
        sql = """select * from registros"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [Regists(**item) for item in data]
        return users

    def get_regist_by_id(self, id):
        sql = """SELECT * FROM registros WHERE id= :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Regists(
                id= data['id'],
                email= data['email'],
                password= data['password']
            )

        return user

    def get_by_email_and_password(self, email, password):
        sql = """SELECT * FROM registros WHERE email= :email AND password= :password"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"email": email, "password": password})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Regists(
                id= data['id'],
                email= data['email'],
                password= data['password']
            )

        return user

    def save(self, user):
        sql = """insert into registros (id, email, password) values (
            :id, :email, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": user.id, "email": user.email, "password": user.password}
            # { **user.to_dict(), 'password': user.password}
        )
        conn.commit()



