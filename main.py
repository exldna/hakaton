from source.bot import MasterBot
from source.database import DataBase

def main():
    db = DataBase()
    db.create_tables()
    db.insert_private_info()

    master_bot = MasterBot(db)
    master_bot.start()


if __name__ == "__main__":
    main()
