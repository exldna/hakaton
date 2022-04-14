from source.bot import Bot
from source.database import DataBase
from source.interaction import Interaction

def main():
    db = DataBase()
    act = Interaction(db)
    bot = Bot(act)
    bot.start()

if __name__ == "__main__":
    main()
