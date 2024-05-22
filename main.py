#!/usr/bin/env python3
import requests

def telegram_bot_sendtext(bot_message, bot_chatID):

   bot_token = ''
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

vpn_users = open('vpn_users', 'r').readlines()

for user_id in vpn_users:
   send_msg = telegram_bot_sendtext("Привет! 👋 \nЧерез 10 минут начнутся технические работы, VPN будет недоступен примерно 1 час.\n\nОб окончании работ будет сообщено здесь.", user_id)
   send_msg = telegram_bot_sendtext("Работа VPN восстановлена! \n\n**Что нового:** \n- Появилась возможность смотреть TikTok через VPN\n- Улучшена производительность VPN-сервера", user_id)
   print(send_msg)