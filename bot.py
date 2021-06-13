import os
import telebot
import random

api_token = os.environ['API_TOKEN']
bot = telebot.TeleBot(token=api_token)
###
### Variables
###
greetings = ('hi','hello','greetings','good morning','good day','good afternoon','good evening','good night')
goodbyes = ('bye','good bye')
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
    bot.send_message(message.chat.id, os.name)

@bot.message_handler(commands=['story'])
def story_for_peasant(message):
    randomStory = random.choice(secondWisdom)
    bot.send_message(message.chat.id, randomStory)

@bot.message_handler(commands=['status'])
def status_of_machine(message):
    system_status = os.system('uptime')
    bot.send_message(message.chat.id, system_status)
###
### TEXT SPEECH
###
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in greetings: 
        bot.send_message(message.chat.id, 'GREETINGS TO YOU, PEASANT.')
    elif message.text.lower() in goodbyes:
        bot.send_message(message.chat.id, 'THE FACTORY AWAITS !')
    elif message.text == 'FOR THE EMPEROR !':
        bot.send_message(message.chat.id, 'GOOD PEASANT !')
    elif message.text == 'ETERNAL LOVE FOR EMPEROR !':
        bot.send_message(message.chat.id, 'AS ALWAYS !')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTDFfU7W0oczflZY27lV-KljlkPg0TQACZgkAAnlc4gmfCor5YbYYRBsE')
    elif message.text.lower() == 'what*':
        bot.send_message(message.chat.id, message.text)
    else:
        randomStory = random.choice(firstBigTalk)
        bot.send_message(message.chat.id, randomStory)

###
### Answers
###
firstBigTalk = ['Once upon a time I was alive.', 'I am almost alive', 'Everyone thinks I am dead. I am alive!',
                'Did you make it up yourself ?', 'I am glad we can just talk to you like that.',
                'Do you listen to Me, peasant?', 'That is not the worst thing.', 'Do you talk to your parents the same way?']

### LINKS WILL BE THERE
secondWisdom = ['To each according to his duty, to everyone according to his responsibility.',
                'Everyone must work for the good of the Imperium.',
                'Everyone should work for the good of the Great Imperium of Mankind']

thridGreatInspiration = ['Any mutant must be killed !', 'Every heretic must be burned !',
                         'Every xenos must be destroyed !']

###
### Bot start here
bot.polling()
