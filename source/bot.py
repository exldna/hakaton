from telebot import TeleBot

from .database import DataBase

from .interaction import \
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
        def handler(message):
            # TODO: написать нормальный хендлер (парсить сообщения, а не строки)
            print("handle message:", message.text)
            comm = message.text.split(" ")
            match comm[0]:
                case "start":
                    if len(comm) != 1:
                        self.bot.send_message(
                            message.chat.id, "Failed: неправильное количество аргументов команды")
                        return
                    err_c = self.act.create_user(message.from_user.username)
                    msg = self.act.parse_err("create_user", err_c)
                case "create":
                    if len(comm) != 2:
                        self.bot.send_message(
                            message.chat.id, "Failed: неправильное количество аргументов команды")
                        return
                    err_c = self.act.create_event(
                        message.from_user.username, comm[1], "", True)
                    msg = self.act.parse_err("create_event", err_c)
                case "plan":
                    if len(comm) != 3:
                        self.bot.send_message(
                            message.chat.id, "Failed: неправильное количество аргументов команды")
                        return
                    err_c = self.act.plan_event(
                        message.from_user.username, comm[1], comm[2])
                    msg = self.act.parse_err("plan_event", err_c)
                case "subscribe":
                    if len(comm) != 3:
                        self.bot.send_message(
                            message.chat.id, "Failed: неправильное количество аргументов команды")
                        return
                    err_c = self.act.subscribe(
                        message.from_user.username, comm[1])
                    msg = self.act.parse_err("plan_event", err_c)
                case _:
                    msg = "Я не знаю такой команды!"
            self.bot.send_message(message.chat.id, msg)


class LinkerBot(Bot):
    def __init__(self, db: DataBase) -> None:
        self.act = LinkerInteraction(db)
        super().__init__(self.act.get_token())
