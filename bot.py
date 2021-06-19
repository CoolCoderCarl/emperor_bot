import os
import telebot
import random
import items.big_talk
import items.eternal_wisdom

# api_token = os.environ['API_TOKEN']
bot = telebot.TeleBot(token="1802734430:AAHESIJUGFg8d6P_OpF-w1BO_vgl0n0FzzI")
###
### Variables
###
greetings = ('hi','hello','greetings','good morning','good day','good afternoon','good evening','good night')
goodbyes = ('bye','good bye','good luck','farewell','till','till next time', 'see you soon')
examples = ('For the Emperor !','Eternal love for the Emperor !')
###
### Buttons for the Honor of the Emperor
###
keyForTheEmperor = telebot.types.ReplyKeyboardMarkup(True, True)
keyForTheEmperor.row('I LOVE YOU EMPEROR !')

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
    	Hello ! Send /wisdom or /wisdom@god_emperor_bot and have fun.
    	""")

    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['wisdom'])
def story_for_peasant(message):
    randomWisdom = random.choice(items.eternal_wisdom.eternal_wisdom)
    bot.send_message(message.chat.id, randomWisdom)

    bot.send_poll(message.chat.id, "Do you like this joke ?",
                  ["Yes !", "Yes of course !", "FOR THE EMPEROR !"],
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
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, 'Greeting to you, peasant.')
    elif message.text.lower() in goodbyes:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, 'The factory awaits !')
    elif message.text.lower() in examples:
        bot.send_message(message.chat.id, 'Good peasant !')
    elif message.text.lower() in examples:
        bot.send_message(message.chat.id, 'As always !')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTDFfU7W0oczflZY27lV-KljlkPg0TQACZgkAAnlc4gmfCor5YbYYRBsE')
    else:
        randomAnswer = random.choice(items.big_talk.big_talk)
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, randomAnswer)

###
### Bot start here
bot.polling()
