import telebot 
from telebot import types 
 
bot = telebot.TeleBot('5873726528:AAFY5G4Z_qNnyIyBTzGZzWrKyDXY5M0m_b8') 
 
 
@bot.message_handler(commands=['start']) 
def start_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("Я знаю, что купить") 
    btn2 = types.KeyboardButton("Я пока не знаю, что купить") 
    markup.add(btn1, btn2) 
    bot.send_message(message.chat.id, text="Здравствуйте! Я бот-консультант. Подскажите, знаете ли вы, что вы хотите приобрести?".format(message.from_user), reply_markup=markup) 
    
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Я знаю, что купить":
        bot.send_message(message.chat.id, text="Заебись")
    else:
        bot.send_message(message.chat.id, text="Хуево")  
 
@bot.message_handler(content_types=["new_chat_members"]) 
def foo(message): 
    user_name = message.new_chat_members[0].username 
    bot.reply_to(message, f"welcome @{user_name}") 
    bot.send_photo(message.chat.id, open("C://Users//Roma//Desktop//photo_2023-01-13_13-23-27 (2).jpg", 'rb'), caption='Джими рад тебя видеть') 
bot.polling(none_stop=True)