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

    def start(self) -> None:
        self.bot.infinity_polling()


class MasterBot(Bot):
    def __init__(self, db: DataBase) -> None:
        self.act = MasterInteraction(db)
        super().__init__(self.act.get_token())

        @self.bot.message_handler(content_types=["text"])
        def say_hello(message):
            comm = message.text.split(" ")
            match comm[0]:
                case "start":
                    self.act.create_user(message.from_user.username)
                    self.bot.send_message(message.chat.id, "hello")
                case "create":
                    if len(comm) != 2:
                        self.bot.send_message(
                            message.chat.id, "filed: wrong args nums")
                    self.act.create_event(
                        [message.from_user.username], comm[1])


class LinkerBot(Bot):
    def __init__(self, db: DataBase) -> None:
        self.act = LinkerInteraction(db)
        super().__init__(self.act.get_token())
