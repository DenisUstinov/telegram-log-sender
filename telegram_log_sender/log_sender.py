import os
import requests
from retry import retry

class TelegramLogSender:
    def __init__(self, bot_token, chat_id, separator=" "):
        """
        Инициализирует отправителя логов в Telegram.
        
        :param bot_token: Токен бота для API Telegram.
        :param chat_id: ID чата для отправки сообщений.
        :param separator: Разделитель для сообщений, по умолчанию пробел.
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.separator = separator
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    @retry(tries=3, delay=2, backoff=2)
    def send_log(self, log_messages, notify=True):
        """
        Отправляет список логов в Telegram в виде одного сообщения, разделенного заданным сепаратором.
        
        :param log_messages: Список строковых сообщений для отправки.
        :param notify: Флаг, отправлять ли сообщение с уведомлением (True) или без уведомления (False).
        """
        log_message = self.separator.join(log_messages)
        
        payload = {
            'chat_id': self.chat_id,
            'text': log_message,
            'disable_notification': not notify
        }
        
        try:
            response = requests.get(self.base_url, params=payload)
            if response.status_code != 200:
                raise Exception(f"Error sending message: {response.text}")
            return response.json()
        
        except Exception as e:
            print(f"Failed to send log: {str(e)}")
            raise

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    logger = TelegramLogSender(bot_token, chat_id, separator=" | ")

    log_messages = [
        "#t01102024235723",
        "#aiogramdispatcher",
        "#INFO : Run polling for bot @my_timekeeper_bot id=7516136139 - 'Timekeeper'"
    ]
    
    try:
        response = logger.send_log(log_messages)
        print("Log sent:", response)
    except Exception as e:
        print("An error occurred while sending the log:", str(e))