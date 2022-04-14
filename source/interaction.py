from .database import DataBase

class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db

    def find_user(self, id):
        return
    

    def add_personal_event(self, user):
        pass

    def add_group_event(self, group):
        pass
