import telegram


class Telegram:

    def __init__(self, token: str):
        self.bot = telegram.Bot(token=token)
        self.offset = 0

    @property
    def updates(self):
        try:
            messages = self.bot.get_updates(offset=self.offset)
        except:
            messages = []
        if messages:
            self.offset = messages[-1]['update_id'] + 1
        return messages

    def send(self, chat_id, message):
        self.bot.send_message(chat_id=chat_id, text=message)

