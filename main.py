import telebot

from parse.Parse import Parse
from parse.dataPy import Data

# ----------------------------------------- SETINGS -----------------------------------------
URL_USD = 'https://banki24.by/minsk/kurs/usd'
URL_EUR = 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
URL_PLN = 'https://banki24.by/minsk/kurs/pln'

TOKEN = 'ПОЛУЧАЕТЕ ТОКЕН И ВСТАВЛЯЕТЕ СЮДА'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'
BUTTON_PLN = 'PLN'

BUTTON_GET_ALL_LIST = 'Вывести весь список банков'
BUTTON_BEST_BUY_VALUE = 'Вывести лучший курс для покупки'
BUTTON_BEST_SELL_VALUE = 'Вывести лучший курс для продажи'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR)
KEYBOARD_START.row(BUTTON_RUB, BUTTON_PLN)

KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST)
KEYBOARD_CHOICE.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE)
KEYBOARD_CHOICE.row(BUTTON_START)
# ----------------------------------------------------------------------

@BOT.message_handler(commands=['start'])
def start_message(message):
    BOT.send_message(message.chat.id, 'Выберите интересующую вас валюту', reply_markup=KEYBOARD_START)

@BOT.message_handler(content_types=['text'])
def get_text_messages(message):

    global site, values
    
    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_RUB:
        site = Parse(URL_RUB).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_PLN:
        site = Parse(URL_PLN).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_ALL_LIST:
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        BOT.send_message(message.chat.id, values.get_best_buy_value(), reply_markup=KEYBOARD_CHOICE)
    
    elif message.text == BUTTON_BEST_SELL_VALUE:
        BOT.send_message(message.chat.id, values.get_best_sell_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)

    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю :( Напиши, пожалуйста, /start')

BOT.polling()
