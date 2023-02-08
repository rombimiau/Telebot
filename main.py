import telebot 
import pandas as pd
from telebot import types 
 
bot = telebot.TeleBot('5873726528:AAFY5G4Z_qNnyIyBTzGZzWrKyDXY5M0m_b8') 
data = pd.read_csv("test_cat.csv")
collections = list(set(data['Коллекция'])) 
 
 
@bot.message_handler(commands=['start']) 
def start_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("Я знаю, что купить") 
    btn2 = types.KeyboardButton("Я пока не знаю, что купить") 
    markup.add(btn1, btn2) 
    bot.send_message(message.chat.id, text="Здравствуйте! Я бот-консультант. Подскажите, знаете ли вы, что вы хотите приобрести?", reply_markup=markup) 
    
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Я знаю, что купить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = []
        for i in collections:
            markup.add(types.KeyboardButton(i))
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Выберите коллекцию", reply_markup=markup)
    elif message.text == "Я пока не знаю, что купить":
        bot.send_message(message.chat.id, text="Эта функция пока недоступна")  
    elif message.text in collections:
        bot.send_message(message.chat.id, text=f"В работе {collections[collections['Коллекция'] == message.text]['Название']}") # тут сделать кнопки с продуктами
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Я знаю, что купить") 
        btn2 = types.KeyboardButton("Я пока не знаю, что купить") 
        markup.add(btn1, btn2) 
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup) 
    
@bot.message_handler(content_types=["new_chat_members"]) 
def foo(message): 
    user_name = message.new_chat_members[0].username 
    bot.reply_to(message, f"welcome @{user_name}") 
    bot.send_photo(message.chat.id, open("C://Users//Roma//Desktop//photo_2023-01-13_13-23-27 (2).jpg", 'rb'), caption='Джими рад тебя видеть') 
bot.polling(none_stop=True)