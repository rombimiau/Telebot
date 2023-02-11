global current_step
global current_catal
global new_markup
global current_good
global current_korzina
current_korzina = {'Название':[], 'Количество':[], 'Цена':[]}
current_step = 0
# mi

def start(message):
    global current_step
    current_step = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Я знаю, что купить")
    btn2 = types.KeyboardButton("Я пока не знаю, что купить")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Здравствуйте! Я бот-консультант. Подскажите, знаете ли вы, что вы хотите приобрести?", reply_markup=markup) 


def first_step(message):
    global current_step
    current_step = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for i in collections:
        markup.add(types.KeyboardButton(i))
    back = types.KeyboardButton("Назад")
    markup.add(back)
    bot.send_message(message.chat.id, text="Выберите коллекцию", reply_markup=markup)
    current_step = 2


def second_step(message):
    global current_step
    global current_catal
    global new_markup
    current_catal = []
    goods_list = []
    new_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(list(data[data['Коллекция'] == message.text]['название']))):
        current_good = list(data[data['Коллекция'] == message.text]['название'])[i]
        bot.send_message(message.chat.id, text=f"{i + 1}. {current_good}. {list(data[data['название'] == current_good]['Наличие'])[0]} в наличии.") # тут сделать кнопки с продуктами
        
        new_markup.add(types.KeyboardButton(list(data[data['Коллекция'] == message.text]['название'])[i]))
    new_markup.add(types.KeyboardButton("Назад"))
    current_catal = list(data[data['Коллекция'] == message.text]['название'])
    bot.send_message(message.chat.id, text="Выберите товар", reply_markup=new_markup)
    current_step = 3

def third_step(message):
    global current_good 
    global new_markup
    global current_step 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Назад"))
    if message.text in current_catal:
        current_good = message.text 
        bot.send_message(message.chat.id, text="Введите количество:", reply_markup=markup)
        current_step = 4
    elif message.text not in current_catal:
        print(message.text, current_catal)
        current_step = 2
    if current_step == 2:
        bot.send_message(message.chat.id, text="В этой коллекции нет такого товара.", reply_markup=markup)
        new_markup.add(types.KeyboardButton(current_catal))
        second_step(message)
    print(message.text, 3)



def fourth_step(message):
    global current_korzina
    global current_step
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Закончить покупки."))
    markup.add(types.KeyboardButton("Продолжить покупки."))
    print(message.text, 4)
    if int(message.text) <= list(data[data['название'] == current_good]['Наличие'])[0]:
        current_korzina['Название'].append(current_good)
        current_korzina['Количество'].append(message.text)
        current_korzina['Цена'].append(list(data[data['название'] == current_good]['Цена '])[0])
        current_step = 5
        bot.send_message(message.chat.id, text="Товар успешно добавлен в корзину. Хотите продолжить покупки?", reply_markup=markup)
    elif int(message.text) > list(data[data['название'] == current_good]['Наличие'])[0]:
        bot.send_message(message.chat.id, text="Столько товара нету в наличии. Введите допустимое значение:", reply_markup=markup)
        current_step = 4


def fifth_step(message):
    global current_step
    if message.text == "Закончить покупки.":
        sum = 0
        response = 'Ваша корзина: \n'
        print(current_korzina)
        for i in range(len(current_korzina['Название'])):
            response += (f'{i + 1}. {current_korzina["Название"][i]}, {current_korzina["Количество"][i]} шт., {current_korzina["Цена"][i]} р. \n')
            sum += (int(current_korzina["Количество"][i]) * int(current_korzina["Цена"][i]))
        response += f'Общая стоимость: {sum} p.'
        bot.send_message(message.chat.id, text=response)
        current_step = 6
    elif message.text == 'Продолжить покупки.':
        current_step = 1
        first_step(message)