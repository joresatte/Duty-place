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
            "password": self.password,
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
            DROP TABLE IF EXISTS registros
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def init_tables(self):
        sql = """
            create table if not exists registros (
                id varchar primary key,
                email varchar,
                password varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from registros"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [Regists(**item) for item in data]
        return users

    def get_by_id(self, id):
        sql = """SELECT * FROM registros WHERE id=: id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Regists(**data)

        return user

    def save(self, category):
        sql = """insert into registros (id, email, password) values (
            :id, :email, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": category.id, "email": category.email, "password": category.password}
            # { **user.to_dict(), 'password': user.password}
        )
        conn.commit()



