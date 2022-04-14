from telebot import TeleBot

class Bot:
    def __init__(self) -> None:
        # TODO: заприватить токен
        self.token = "5378053989:AAFbBy8S8zD5MxSuOBU9eX58LmxefFOkLFA"
        self.bot = TeleBot(self.token)

        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            self.bot.send_message(message.chat.id, "Hi!")

        self.bot.infinity_polling()