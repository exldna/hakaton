from telebot import TeleBot
from .interaction import Interaction

class Bot:
    def __init__(self, act: Interaction) -> None:
        self.act = act

        # TODO: заприватить токен
        self.token = "5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA"
        self.bot = TeleBot(self.token)

        @self.bot.message_handler(commands=["msg"])
        def start_message(message):
            msg = self.act.get_msg()
            self.bot.send_message(message.chat.id, msg)

    def start(self) -> None:
        self.bot.infinity_polling()
