import sqlite3

from threading import Thread
from multiprocessing import Queue

from time import sleep

class DataBase(object):
    def __init__(self, name: str = "db") -> None:

        self.connect = sqlite3.connect(name + ".sqlite", check_same_thread=False)
        self.cursor = self.connect.cursor()

        def run():
            # TODO: multiple cursors
            while self.is_running:
                item = self.queue.get()
                if item != "":
                    self.last_ans = self.__execute(item)
                    self.is_get = False

        # self.queue = Queue()
        # self.thread = Thread(target=run)

        self.is_running = True
        self.is_get = True
        self.last_ans = None

        # self.thread.start()

    def __del__(self) -> None:
        # TODO: блокировка!
        self.connect.close()
        self.is_running = False
        # self.thread.join()
        # self.queue.close()

    def __execute(self, request: str):
        # self.queue.put(request)
        return self.get()

    def get(self):
        while self.is_get:
            sleep(0.01)
        self.is_get = True
        return self.last_ans

    def execute(self, request: str):
        self.cursor.execute(request)
        self.connect.commit()
        return self.cursor.fetchall()

    
