import telepot
import time




def handle(msg):

    chat_id = msg['chat']['id']
    command = msg['text']
    print(msg)


    if command == '/start':
        bot.sendMessage(chat_id,'hello the bot is started')

    if command == '/wel':
        bot.sendMessage(chat_id,'Wellcome')


bot=telepot.Bot('your tkoen bot')
bot.message_loop(handle)

while (1):
    time.sleep(10)
    
