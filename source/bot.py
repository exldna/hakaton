from telebot import TeleBot
from telebot import types as tb_types

from .database import DataBase

from .interaction import \
    Interaction, \
    MasterInteraction, \
    LinkerInteraction


class Bot(object):
    def __init__(self, token: str) -> None:
        self.bot = TeleBot(token)

    def polling(self) -> None:
        self.bot.polling()



class MasterBot(Bot):
    def __init__(self, db: DataBase) -> None:
        self.act = MasterInteraction(db)
        super().__init__(self.act.get_token())

        @self.bot.message_handler(commands=["hello"])
        def say_hello(message):
            self.bot.send_message(message.chat.id, "hi!")

class LinkerBot(Bot):
    def __init__(self, db: DataBase) -> None:
        self.act = LinkerInteraction(db)
        super().__init__(self.act.get_token())
