import requests
from bs4 import BeautifulSoup as Bs
import requests
from telebot import types
import telebot


token = '6061519738:AAHLD1XpUXMF4V60RLBxzlKbEns7zMSN80U'
url = 'https://www.binance.com/ru-UA/price/bitcoin'

r = requests.get(url)

soup = Bs(r.text, 'html.parser')

bitok = soup.find_all('div', class_='css-12ujz79')

clear_bitok = [i.text for i in bitok]
print(clear_bitok)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start (massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('❤')
    item2 = types.KeyboardButton('👎')
    item3 = types.KeyboardButton('💤')


    markup.add(item1, item2, item3)


    bot.send_message(massage.chat.id, "привет", reply_markup=markup )

@bot.message_handler(commands=['menu'])
def show_menu(message):
    menu = "1. Вывести цену биткоина\n2. Показать другие криптовалюты"
    bot.send_message(message.chat.id, menu)

@bot.message_handler(func=lambda message: message.text == '1')
def show_btc_price(message):
    if len(clear_bitok) > 0:
        bot.send_message(message.chat.id, clear_bitok[0])
        del clear_bitok[0]
    else:
        bot.send_message(message.chat.id, 'Извините, цены на биткоин временно недоступны. Попробуйте позже.')

@bot.message_handler(func=lambda message: message.text == '2')
def show_other_crypto(message):
    # TODO: добавить обработчик для показа других криптовалют
    bot.send_message(message.chat.id, 'К сожалению, эта функция еще не реализована.')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Извините, я не понимаю эту команду. Пожалуйста, используйте команду /menu, чтобы открыть меню.')

@bot.message_handler(commands=['menu'])
def menu(massage):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/menu')
    bot.send_message(massage.chat.id, 'Добро пожаловать', reply_markup=user_markup)



bot.polling()









