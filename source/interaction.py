from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                Hello TEXT
            );
            """
        )
        db.execute(
            """
            INSERT INTO users(Hello) VALUES ('Привет!');
            """
        )

    def get_msg(self) -> str:
        answer = str(self.db.execute("SELECT Hello from users"))
        print(answer)
        return answer

    def create_user(self):
        self.db.execute("INSERT users(")
