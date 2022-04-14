from telebot import TeleBot
from .database import DataBase

class Bot:
    def __init__(self, db: DataBase) -> None:

        self.db = db

        # TODO: заприватить токен
        self.token = "5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA"
        self.bot = TeleBot(self.token)

        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            self.bot.send_message(message.chat.id, "Hi!")

    def start(self) -> None:
        self.bot.infinity_polling()
