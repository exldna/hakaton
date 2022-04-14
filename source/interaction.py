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






=======
>>>>>>> 4dbea877fb2a3f3e86b2289283fa0c1e6c7adc6f
