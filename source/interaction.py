from .database import DataBase


class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db

        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                name TEXT,
                subscribed_events integer ARRAY,
                events integer ARRAY
            );
            """
        )
        
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS events(
                title TEXT,
                description TEXT,
                datetime DATETIME,
                subscribed_users integer ARRAY,
                owner_id INT,
                is_pubic BOOlEAN
            );
            """
        )

        db.execute(
            """
            CREATE TABLE IF NOT EXISTS event_types(
                title TEXT,
                description TEXT,
                owner_id INT,
                is_pubic BOOlEAN
            );
            """
        )

    def get_token(self) -> str:
        raise NotImplementedError(
            "you must implement get_token to use Interaction child")


class MasterInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT master_token FROM private_info;
        """)
        return token[0][0]

    def create_user(self, usr_name: str):
        if self.db.execute(f"SELECT name FROM users WHERE name = '{usr_name}';"):
            return
        self.db.execute(
            "INSERT INTO users(name) VAlUES({})".format(usr_name, "{}", "{}"))

    def create_event(self, users: list, event: str) -> None:
        for user in users:
            self.db.execute(
                "INSERT INTO users(active_events) VALUES({}) WHERE name={};".format(event, user))
            self.db.execute(
                "INSERT INTO users(personal_events) VALUES({}) WHERE name={};".format(event, user))

    def get_event(self, user: str, datetime) -> str:
        answer = str(self.db.execute(
            """SELECT active_events FROM users WHERE;"""))
        return answer

    @property
    def get_user(self) -> str:
        answer = str(self.db.execute("SELECT * FROM users"))
        return answer


class LinkerInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT linker_token FROM private_info;
        """)
        return token[0][0]
