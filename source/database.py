from multiprocessing import Queue, Process, Pipe
from sqlite3 import connect as sqlite3_conn


def runner(queue: Queue, pipe, name: str) -> None:
    with sqlite3_conn(name + ".sqlite", check_same_thread=False) as connect:
        cursor = connect.cursor()
        while True:
            command = queue.get()
            cursor.execute(command)
            connect.commit()
            pipe.send(cursor.fetchall())


class DataBase(object):
    def __init__(self, name: str = "db") -> None:
        self.name = name
        self.queue = Queue()
        self.pipe_in, self.pipe_out = Pipe()
        self.process = Process(target=runner, args=(
            self.queue, self.pipe_in, self.name,))
        self.process.start()

    def __del__(self) -> None:
        self.queue.close()
        self.pipe_in.close()
        self.pipe_out.close()
        self.process.terminate()

    def execute(self, command: str):
        self.queue.put(command)
        return self.pipe_out.recv()

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
