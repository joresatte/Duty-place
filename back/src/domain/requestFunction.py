from src.domain.utils import Utils

class Request:
    def __init__(self, id, name, email, subject, comments):
        self.id= id
        self.name= name
        self.email= email
        self.subject= subject
        self.comments= comments
    
class RequestRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def __enter__(self):
         return self.init_tables()
    
    def __exit__(self, type, value, traceback):
        self.init_tables().close()
        return True

    def create_conn(self):
        conn= Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.createTable(self, tables_variables= ['id', 'name', 'email', 'subject', 'comments'], tableName= "requestables")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def save(self, request):
        sql= Utils.getFullSaveDynamicQuery(self, table_variables= ['id', 'name', 'email', 'subject', 'comments'], tableName= "requestables")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id, "name": request.name, "email": request.email, "subject": request.subject, "comments": request.comments}
        )
        conn.commit()
