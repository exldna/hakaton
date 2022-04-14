import sqlite3

class DataBase(object):
    def __init__(self, name: str = "db") -> None:
        self.connect = sqlite3.connect(name + ".sqlite", check_same_thread=False)
        self.cursor = self.connect.cursor()

    def __del__(self) -> None:
        self.connect.close()

    def execute(self, request: str):
        self.cursor.execute(request)
        self.connect.commit()
        return self.cursor.fetchall()
