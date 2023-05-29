class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


if __name__ == '__main__':
    name = "Niko"
    some_bot = Bot(name)
    some_bot.say_name()
    some_bot.send_message("Hello")

    telegram_name = "TG"
    telegram_bot = TelegramBot(telegram_name)
    telegram_bot.say_name()
    telegram_bot.send_message('Hello')
    telegram_bot.set_chat_id(1)
    telegram_bot.set_url("https://example.com")
    telegram_bot.send_message('Hello')

