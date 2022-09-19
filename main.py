import os
import telebot
#add api key
api_key = os.environ['API_KEY']

#bot
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["start"])
def welcome(message):
    msg = """Welcome to Ombre Nore the image generator bot 😁"""
    bot.reply_to(message, msg)


print("Running the bot")
bot.infinity_polling()
