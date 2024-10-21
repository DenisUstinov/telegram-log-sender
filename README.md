# Telegram Log Sender

`telegram-log-sender` — это Python модуль, который отправляет логи в Telegram с использованием бота. Он поддерживает отправку логов с возможностью настройки уведомлений (с или без уведомления) и повторных попыток в случае ошибки.

## Установка

Вы можете установить этот модуль через `pip` из исходников или локальной папки:

1. Склонируйте репозиторий:

```bash
git clone https://github.com/DenisUstinov/telegram-log-sender.git
```

2. Перейдите в директорию проекта:
```bash
cd telegram_log_sender
```

3. Установите модуль с помощью pip:
```bash
pip install
```

Или, если вы хотите установить через pip в другом проекте:
```bash
pip install git+https://github.com/DenisUstinov/telegram-log-sender.git
```
## Использование

После установки модуля, вы можете использовать его в своем Python коде для отправки логов в Telegram.

```python
import os
from telegram_log_sender import TelegramLogSender

# Пример использования
if __name__ == "__main__":
    # Убедитесь, что у вас есть значения для переменных окружения
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    logger = TelegramLogSender(bot_token, chat_id, separator=" | ")

    log_messages = [
        "#t01102024235723",
        "#aiogramdispatcher",
        "#INFO : Run polling for bot @my_timekeeper_bot id=7516136139 - 'Timekeeper'"
    ]
    
    try:
        response = logger.send_log(log_messages, notify=True)  # Отправить сообщение с уведомлением
        print("Log sent:", response)
    except Exception as e:
        print("An error occurred while sending the log:", str(e))
```

Параметры:

- **bot_token**: Токен вашего Telegram-бота (его можно передавать через переменные окружения или напрямую).
- **chat_id**: ID чата, куда вы хотите отправить сообщение (его также можно передавать через переменные окружения или напрямую).
- **separator**: Строка-разделитель для объединения сообщений в одно (по умолчанию пробел).
- **notify**: Булевый флаг, определяющий, будет ли сообщение отправлено с уведомлением (True) или без уведомления (False).

### Переменные окружения

Если вы хотите использовать переменные окружения для передачи токена бота и ID чата, добавьте их в .env файл или настройте в вашей системе:

```bash
export BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
export CHAT_ID='YOUR_TELEGRAM_CHAT_ID'
```

## Особенности
При использовании модуля стоит помнить о некоторых особенностях.

### Повторные попытки
В случае ошибки отправки логов, модуль автоматически выполнит до 3 повторных попыток с увеличивающейся задержкой (2 секунды между первой и второй попыткой, 4 секунды между второй и третьей).

### Отправка без уведомления

Опция notify позволяет отключить уведомления для сообщений, если это необходимо.

## Лицензия

Этот проект лицензирован под лицензией MIT.