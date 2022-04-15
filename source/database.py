import sqlite3

# from threading import Thread
# from multiprocessing import Queue

# from time import sleep


class DataBase(object):
    # TODO: write thread-safety DB
    # TODO: create DB backgrounds

    def __init__(self, name: str = "db") -> None:
        self.connect = sqlite3.connect(
            name + ".sqlite", check_same_thread=False)

        self.cursor = self.connect.cursor()

        # def run():
        # TODO: multiple cursors
        # while self.is_running:
        # item = self.queue.get()
        # if item != "":
        # self.last_ans = self.__execute(item)
        # self.is_get = False

        # self.queue = Queue()
        # self.thread = Thread(target=run)

        # self.is_running = True
        # self.is_get = True
        # self.last_ans = None

        # self.thread.start()

    def __del__(self) -> None:
        self.connect.close()
        # TODO: блокировка!
        # self.is_running = False
        # self.thread.join()
        # self.queue.close()

    def execute(self, request: str):
        self.cursor.execute(request)
        self.connect.commit()
        return self.cursor.fetchall()

    def create_tables(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                events integer ARRAY,
                subscribed_events integer ARRAY
            );
        """)

        self.execute("""
            CREATE TABLE IF NOT EXISTS events(
                id INTEGER PRIMARY KEY,
                base_type INT UNSIGNED NOT NULL,
                datetime DATETIME,
                subscribed_users integer ARRAY
            );
        """)

        self.execute("""
            CREATE TABLE IF NOT EXISTS event_types(
                id INTEGER PRIMARY KEY,
                owner INT UNSIGNED NOT NULL,
                name TEXT,
                description TEXT,
                is_pubic BOOlEAN
            );
        """)

    def insert_private_info(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS private_info(
                master_token TEXT,
                linker_token TEXT
            );
        """)

        self.execute("""
            INSERT INTO private_info(master_token, linker_token) 
            VALUES (
                '5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA',
                '5157776609:AAGVT7kYK_ep0Ezu3Fz2-tcav7lfAe1poDQ'
            );
        """)

    # def __execute(self, request: str):
        # self.queue.put(request)
        # return self.get()

    # def get(self):
        # while self.is_get:
        # sleep(0.01)
        # self.is_get = True
        # return self.last_ans
