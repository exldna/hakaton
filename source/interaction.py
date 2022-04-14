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
        self.db.execute("INSERT INTO users(name) VAlUES({})".format(name, None, None))

    @property
    def get_user(self) -> str:
        answer = str(self.db.execute("SELECT * FROM users;"))
        return answer

    def set_event(self, username: str, event:str)->None:
        self.db.execute("INSERT INTO users(active_events) VALUES({}) WHERE name={};".format(event, username))

    def create_event(self, users: list, event: str) -> None:
        for user in users:
            self.db.execute("INSERT INTO users(active_events) VALUES({}) WHERE name={};".format(event, user))
            self.db.execute("INSERT INTO users(personal_events) VALUES({}) WHERE name={};".format(event, user))

    def get_event(self, user: str, datetime)->str:
        answer = str(self.db.execute("""SELECT active_events FROM users WHERE ;"""))
        return answer


