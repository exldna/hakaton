from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db

    def get_msg(self) -> str:
        return "pass"
