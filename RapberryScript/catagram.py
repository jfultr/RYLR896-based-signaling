import requests


class TelegramBot(object):

    def __init__(self):
        super(TelegramBot, self).__init__()
        self.chat_ids = [
            386830039,
            426538860
        ]

    def url_and_bot_token(self):
        return 'https://api.telegram.org/bot579887627:AAHfX87fq8VRVU777sY7d9GQXocZUbV_qvI'

    def send_img(self, img, bot_message):
        status = ''
        for chats in self.chat_ids:
            status += self.send_img_to(img, bot_message, chats)
            img.seek(0)
        return status

    def send_text(self, bot_message):
        status = ''
        for chats in self.chat_ids:
            status = self.send_text_to(bot_message, chats)
        return status

    def send_text_to(self, bot_message, bot_chatID):
        url = self.url_and_bot_token() + '/sendMessage'
        data = {'chat_id': str(bot_chatID),
                'parse_mode': 'Markdown',
                'text': bot_message,
                'disable_notification': True
                }
        response = requests.post(url=url, data=data)
        return response.json()

    def send_img_to(self, img, bot_message, bot_chatID):
        data = {'chat_id': bot_chatID,
                # 'caption': bot_message,
                'parse_mode': 'Markdown',
                'disable_notification': True}
        files = {'photo': img}
        url = self.url_and_bot_token() + '/sendPhoto'
        response = requests.post(url=url, data=data, files=files)
        return response.json()
