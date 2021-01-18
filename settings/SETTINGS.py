import telebot
URL_USD = 'https://banki24.by/minsk/kurs/usd'
URL_EUR = 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
TOKEN = '1505553964:AAGJwY-XxYNTQ7uEAavia_RmRlxZiKBgx3k'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'

BUTTON_GET_ALL_LIST = 'Вывести весь список банков'
BUTTON_BEST_BAY_VALUE = 'Вывести лучший курс для покупки'
BUTTON_BEST_SELL_VALUE='Вывести лучший курс для продажи'



def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR)
KEYBOARD_START.row(BUTTON_RUB)

KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row( BUTTON_GET_ALL_LIST,BUTTON_BEST_BAY_VALUE)
KEYBOARD_CHOICE.row(BUTTON_BEST_SELL_VALUE,BUTTON_START)