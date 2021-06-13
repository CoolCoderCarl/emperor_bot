import os
import telebot
import random
import items.big_talk
import items.eternal_wisdom

api_token = os.environ['API_TOKEN']
bot = telebot.TeleBot(token=api_token)
###
### Variables
###
greetings = ('hi','hello','greetings','good morning','good day','good afternoon','good evening','good night')
goodbyes = ('bye','good bye','good luck')
###
### Buttons for the Honor of the Emperor
###
keyForTheEmperor = telebot.types.ReplyKeyboardMarkup(True, True)
keyForTheEmperor.row('FOR THE EMPEROR !', 'ETERNAL LOVE FOR EMPEROR !')

###
### Basic commands
###
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'I AM HERE TO GUIDE YOU THROUGH THIS DARK TIMES, PEASANT.',
                     reply_markup=keyForTheEmperor)

@bot.message_handler(commands=['help'])
def help_to_peasant(message):

    welcome = ("""
    	Hello ! Send /wisdom and have fun.
    	""")

    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['wisdom'])
def story_for_peasant(message):
    randomStory = random.choice(items.eternal_wisdom)
    bot.send_message(message.chat.id, randomStory)

    bot.send_poll(message.chat.id, "Do you like this joke ?",
                  ["Yes !", "Yes of course !", "FOR THE EMPEROR !", "ETERNAL LOVE FOR EMPEROR !"],
                  is_anonymous=False)

###
### Poll about every important things will be here
###
# @bot.message_handler(commands=['status'])
# def status_of_machine(message):
#     system_status = os.system('uptime')
#     bot.send_message(message.chat.id, system_status)
###
### Text speech
###
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in greetings: 
        bot.send_message(message.chat.id, 'GREETINGS TO YOU, PEASANT.')
    elif message.text.lower() in goodbyes:
        bot.send_message(message.chat.id, 'THE FACTORY AWAITS !')
    elif message.text.lower() == 'FOR THE EMPEROR !':
        bot.send_message(message.chat.id, 'GOOD PEASANT !')
    elif message.text.lower() == 'ETERNAL LOVE FOR EMPEROR !':
        bot.send_message(message.chat.id, 'AS ALWAYS !')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTDFfU7W0oczflZY27lV-KljlkPg0TQACZgkAAnlc4gmfCor5YbYYRBsE')
    else:
        randomStory = random.choice(items.big_talk)
        bot.send_message(message.chat.id, randomStory)

###
### Bot start here
bot.polling()
