from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS hello(
                Hello TEXT
            );
            """
        )
        db.execute(
            """
                CREATE TABLE IF NOT EXISTS users(
                    id INT,
                    name TEXT,
                    personal_events TEXT,
                    active_events TEXT
                );
            """
        )
        db.execute("""
            TRUNCATE TABLE hello;
        """)
        # db.execute(
        #     """
        #     INSERT INTO users(Hello) VALUES ('Привет!');
        #     """
        # )

    def get_msg(self) -> str:
        answer = str(self.db.execute("SELECT Hello from hello"))
        print(answer)
        return answer

    def create_user(self):
        self.db.execute("INSERT users(")


