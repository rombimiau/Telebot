import telebot

bot = telebot.TeleBot('5873726528:AAFY5G4Z_qNnyIyBTzGZzWrKyDXY5M0m_b8')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет iuhiub привет ✌️ ")


@bot.message_handler(content_types=["new_chat_members"])
def foo(message):
    user_name = message.new_chat_members[0].username
    bot.reply_to(message, f"welcome @{user_name}")
    bot.send_photo(message.chat.id, open("C://Users//Roma//Desktop//photo_2023-01-13_13-23-27 (2).jpg", 'rb'), caption='Джими рад тебя видеть')
bot.polling(none_stop=True)
