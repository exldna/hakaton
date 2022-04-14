from source.bot import Bot
from source.database import DataBase

def main():
    db = DataBase()
    bot = Bot(db)
    bot.start()

if __name__ == "__main__":
    main()
