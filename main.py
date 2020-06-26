import telebot
import random

bot = telebot.TeleBot(token='1263231073:AAGvUob4MTimlFzAKfdLDTjySnpxEhnHqxg')
###
### BUTTON FOR THE HONOR OF THE EMPERROR
###
keyForTheEmperor = telebot.types.ReplyKeyboardMarkup(True)
keyForTheEmperor.row('ЗА ИМПЕРАТОРА !')
###
### BASIC COMMANDS
###
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Я ЗДЕСЬ ДЛЯ ТОГО ЧТОБЫ ВЕСТИ ТЕБЯ В ЭТО ТЁМНОЕ ВРЕМЯ, КРЕСТЬЯНИН.',
                     reply_markup=keyForTheEmperor)

@bot.message_handler(commands=['help'])
def help_to_peasant(message):
    bot.send_message(message.chat.id, 'ПРОСИ ЧТО УГОДНО !')

@bot.message_handler(commands=['story'])
def story_for_peasant(message):
    randomStory = random.choice(secondWisdom)
    bot.send_message(message.chat.id, randomStory)
###
### TEXT SPEECH
###
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == ('Привет'):
        bot.send_message(message.chat.id, 'ПРИВЕТСТВУЮ ТЕБЯ, КРЕСТЬЯНИН.')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'ЗАВОД ЖДЁТ !')
    elif message.text == 'ЗА ИМПЕРАТОРА !':
        bot.send_message(message.chat.id, 'ХОРОШИЙ КРЕСТЬЯНИН !')
    else:
        randomStory = random.choice(firstBigTalk)
        bot.send_message(message.chat.id, randomStory)

###
### ANSWERS
###
firstBigTalk = ['Когда то и я был живым', 'Я почти жив', 'Все думают что я мёртв. А я жив !', 'Ты это сам придумал ?',
                'Рад что мы можем просто так с тобой разговаривать', 'Ты внимаешь Мне, крестьянин ?', 'Бывало и хуже',
                'С родителями ты так же разговариваешь ?']

# LINKS WILL BE THERE
secondWisdom = ['Каждому по обязаности, всякому по ответственности', 'Всякий должен трудиться, на благо Империума',
                'Всякий должен трудиться, во благо Империума', 'Всякий должен трудиться, на благо Великого Империума Человечества']

thridGreatInspiration = ['Всякий мутант должен быть убит !', 'Всякий еретик должен быть сожжён !', 'Всякий ксенов должен быть уничтожен !']

###
### BOT START HERE
bot.polling()
