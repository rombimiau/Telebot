import telebot 
import pandas as pd
from telebot import types 
 
bot = telebot.TeleBot('6014185774:AAHXJvlGhdcsQFvKqU1MQSio9g_NVCcEa34') 
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
        goods_list = []
        new_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(len(list(data[data['Коллекция'] == message.text]['название']))):
            bot.send_message(message.chat.id, text=f"{list(data[data['Коллекция'] == message.text]['название'])[i]}") # тут сделать кнопки с продуктами
            goods_list.append(types.KeyboardButton(list(data[data['Коллекция'] == message.text]['название'])[0]))
            new_markup.add(types.KeyboardButton(list(data[data['Коллекция'] == message.text]['название'])[i]))
        bot.send_message(message.chat.id, text="Выберите товар", reply_markup=new_markup)
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Я знаю, что купить") 
        btn2 = types.KeyboardButton("Я пока не знаю, что купить") 
        markup.add(btn1, btn2) 
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup) 
    
