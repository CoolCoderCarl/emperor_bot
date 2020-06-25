import telebot

bot = telebot.TeleBot(token='1263231073:AAGvUob4MTimlFzAKfdLDTjySnpxEhnHqxg')

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Я ЗДЕСЬ ДЛЯ ТОГО ЧТОБЫ ВЕСТИ ТЕБЯ В ЭТО ТЁМНОЕ ВРЕМЯ, КРЕСТЬЯНИН.")

@bot.message_handler(commands=['help'])
def help_to_peasant(message):
  bot.send_message(message.chat.id, "ПОПРОСИ МЕНЯ И Я РАССКАЖУ ТЕБЕ ИСТОРИЮ.")

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
