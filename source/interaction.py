from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db

    def get_token(self) -> str:
        raise NotImplementedError("you must immplement get_token to use Interaction child")

class MasterInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT master_token FROM private_info;
        """)
        return token[0][0]

    def create_user(self, name: str ):
        self.db.execute("INSERT INTO users(name) VAlUES({})".format(name, None, None))

    @property
    def get_user(self) -> str:
        answer = str(self.db.execute("SELECT * FROM users"))
        return answer

    def set_event(self, username: str, event:str)->None:
        self.db.execute("INSERT INTO users(active_events) VALUES({}) WHERE name={}".format(event, username))

    def create_event(self, users: list, event: str) -> None:
        for user in users:
            self.db.execute("INSERT INTO users(active_events) VALUES({}) WHERE name={}".format(event, user))
            self.db.execute("INSERT INTO users(personal_events) VALUES({}) WHERE name={}".format(event, user))

class LinkerInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT linker_token FROM private_info;
        """)
        return token[0][0]
