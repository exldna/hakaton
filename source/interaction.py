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
                    name TEXT,
                    personal_events TEXT,
                    active_events TEXT
                );
            """
        )
        db.execute(
            """
            INSERT INTO hello(Hello) VALUES ('Привет!');
            """
        )

    def get_msg(self) -> str:
        answer = str(self.db.execute("SELECT Hello from hello"))
        print(answer)
        return answer

    def create_user(self, name: str ):
        self.db.execute("INSERT INTO users(name) VAlUES({})".format(name))

    @property
    def get_user(self) -> str:
        answer = str(self.db.execute("SELECT * FROM users"))
        return answer


