from telebot import TeleBot
from .interaction import Interaction

class Bot:
    def __init__(self, act: Interaction) -> None:
        self.act = act

        # TODO: заприватить токен
        self.token = "5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA"
        self.bot = TeleBot(self.token)

        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            self.bot.send_message(message.chat.id, "Hi!")

    def start(self) -> None:
        self.bot.infinity_polling()
