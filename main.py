from source.bot import MasterBot
from source.database import DataBase

def private_info(db: DataBase):
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS private_info(
            master_token TEXT,
            linker_token TEXT
        );
        """
    )

    db.execute(
        """
        INSERT INTO private_info(master_token, linker_token) 
        VALUES (
            '5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA',
            '5157776609:AAGVT7kYK_ep0Ezu3Fz2-tcav7lfAe1poDQ'
        );
        """
    )

def main():
    db = DataBase()
    # private_info(db)
    master_bot = MasterBot(db)
    master_bot.start()

if __name__ == "__main__":
    main()
