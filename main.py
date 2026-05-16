import telebot
from transliterate import to_cyrillic, to_latin
TOKEN = "8550210902:AAGK9LB6DXV7n3aKd8gRrxrx-0jG038nrpE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Salom, qanday yordam bera olaman?")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    
    if text.isascii():
        bot.reply_to(message, to_cyrillic(text))
    else:
        bot.reply_to(message, to_latin(text))
        
bot.infinity_polling()

# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))