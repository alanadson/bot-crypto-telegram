import telebot
import requests
import json

import lists
import credentials

bot = telebot.TeleBot(credentials.TOKEN)


@bot.message_handler(commands=['Criptomoedas'])
def crypto(message):
    text = lists.list_crypto_text
    bot.reply_to(message, text)  # resp message


# home menu

def check(message):
    return True


@bot.message_handler(func=check)
def reply(message):
    try:
        sigla_crypto = message.text
        sigla_crypto2 = sigla_crypto.strip("/")  # remove the abbreviation bar
        req = requests.get(f'https://www.mercadobitcoin.net/api/{sigla_crypto2}/ticker/')
        cot = json.loads(req.text)
        valor_crypto = float(cot['ticker']['buy'])
        format_valor_crypto = format(valor_crypto, '.2f')
        if valor_crypto > 0:
            bot.send_message(message.chat.id, f'Cotação atual do {sigla_crypto2.upper()} é: {format_valor_crypto}[R$]')

    except:
        text = lists.menu_text
        bot.reply_to(message, text)  # reply message


bot.polling()
