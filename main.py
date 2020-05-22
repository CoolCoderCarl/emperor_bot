import telebot

bot = telebot.TeleBot(token='1263231073:AAGvUob4MTimlFzAKfdLDTjySnpxEhnHqxg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#   bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
      bot.send_message(message.chat.id, 'ПРИВЕТСТВУЮ ТЕБЯ, КРЕСТЬЯНИН.')
    elif message.text == 'Пока':
      bot.send_message(message.chat.id, 'ЗАВОД ЖДЁТ !')
    elif message.text == 'FOR THE EMPEROR !' or 'ЗА ИМПЕРАТОРА !':
      bot.send_message(message.chat.id, 'YEAH !')

bot.polling()
