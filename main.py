import telebot 
import pandas as pd
from telebot import types 
from functions import *
 
bot = telebot.TeleBot('5873726528:AAFY5G4Z_qNnyIyBTzGZzWrKyDXY5M0m_b8') 
data = pd.read_csv("test_cat.csv")
collections = list(set(data['Коллекция'])) 
# print(data[data['Коллекция'] == 'каки']['название'])
    
@bot.message_handler(commands=['start']) 
def start_message(message): 
    start(message)
    


@bot.message_handler(content_types=['text'])
def func(message):
    global current_step
    if message.text == "Я знаю, что купить":
        first_step(message)
    elif message.text == "Я пока не знаю, что купить":
        bot.send_message(message.chat.id, text="Эта функция пока недоступна")
    elif message.text in collections:
        second_step(message)
    elif message.text == "Назад":
        if current_step == 2:
            first_step(message)
        elif current_step == 1:
            start(message)
        elif current_step == 3:
            second_step(message)
        elif current_step == 4:
            third_step(message)
    elif (current_step == 3):
        third_step(message)
    elif current_step == 4:
        fourth_step(message)
    elif current_step == 5:
        fifth_step(message)


bot.polling(none_stop=True)
