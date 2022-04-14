import sqlite3

class DataBase(object):
    def __init__(self, name: str = "db") -> None:
        self.connect = sqlite3.connect(name + ".sqlite", check_same_thread=False)
        self.cursor = self.connect.cursor()

    def __del__(self) -> None:
        self.connect.close()

    def execute(self, request: str) -> None:
        self.cursor.execute(request)
        self.connect.commit()
