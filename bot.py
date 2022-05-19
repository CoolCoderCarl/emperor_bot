import os
import random
from time import sleep

import telebot

import items.big_talk
import items.eternal_wisdom
import items.rank
import items.stickers

api_token = os.environ["API_TOKEN"]
bot = telebot.TeleBot(token=api_token)

# Variables
greetings = (
    "hi",
    "hello",
    "greetings",
    "good morning",
    "good day",
    "good afternoon",
    "good evening",
    "good night",
)
goodbyes = (
    "bye",
    "good bye",
    "good luck",
    "farewell",
    "till",
    "till next time",
    "see you soon",
)

# Buttons for the Honor of the Emperor
# keyForTheEmperor = telebot.types.ReplyKeyboardMarkup(True, True)
# keyForTheEmperor.row('I LOVE YOU EMPEROR !')


# Basic commands
@bot.message_handler(commands=["start"])
def send_welcome(message):

    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(
        message.chat.id, "I AM HERE TO GUIDE YOU THROUGH THIS DARK TIMES, PEASANT."
    )  # , ### Any ideas
    # reply_markup=keyForTheEmperor)


# Instructions
@bot.message_handler(commands=["help"])
def help_to_peasant(message):

    welcome = """
Hello ! Send /wisdom or /wisdom@god_emperor_bot and have fun. \n
Also you can try to check your luck and send /feelpain or /feelpain@god_emperor_bot.
"""

    bot.send_message(message.chat.id, welcome)


# Jokes command
@bot.message_handler(commands=["wisdom"])
def story_for_peasant(message):

    bot.send_chat_action(message.chat.id, "typing")
    random_wisdom = random.choice(items.eternal_wisdom.eternal_wisdom)
    bot.send_message(message.chat.id, random_wisdom)

    bot.send_poll(
        message.chat.id,
        "Do you like this joke ?",
        ["Yes !", "Yes of course !", "FOR THE EMPEROR !"],
        is_anonymous=False,
    )


# Painful command
@bot.message_handler(commands=["feelpain"])
def feel_pain_command(message):
    random_stickers = random.choice(items.stickers.stickers)
    bot.send_message(message.chat.id, "And you are...")
    bot.send_dice(message.chat.id)
    sleep(5)
    random_ranks = random.choice(items.rank.rank)
    bot.send_message(message.chat.id, random_ranks)
    sleep(2)
    bot.send_message(message.chat.id, "As always !")
    sleep(2)
    bot.send_sticker(message.chat.id, random_stickers)


# Text speech
@bot.message_handler(content_types=["text"])
def send_text(message):

    if message.text.lower in greetings:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Greeting to you, peasant.")
    elif message.text.lower in goodbyes:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "The factory awaits !")
    else:
        random_answer = random.choice(items.big_talk.big_talk)
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, random_answer)


# Bot start here
bot.polling()
