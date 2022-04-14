from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db
        db.execute("CREATE TABLE table(Hello, varchar(255)")
        db.execute("INSERT table(Hello) VALUES ('Привет!')")

    def get_msg(self) -> str:
        answer = str(self.db.execute("SELECT Hello from table"))
        return answer

    
