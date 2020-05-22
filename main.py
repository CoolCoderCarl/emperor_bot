import telebot

bot = telebot.TeleBot(token='1263231073:AAGvUob4MTimlFzAKfdLDTjySnpxEhnHqxg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "STOP CLICKING THAT STUPID BUTTONS, PEASANT !")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
      bot.send_message(message.chat.id, 'ПРИВЕТСТВУЮ ТЕБЯ, КРЕСТЬЯНИН.')
    elif message.text == 'Пока':
      bot.send_message(message.chat.id, 'ЗАВОД ЖДЁТ !')
    elif message.text == 'ЗА ИМПЕРАТОРА !':
      bot.send_message(message.chat.id, 'ХОРОШИЙ КРЕСТЬЯНИН !')
    else:
        bot.send_message(message.chat.id, 'ГОВОРИ НОРМАЛЬНО !')

bot.polling()
