import telebot # Importamos las librería
import requests
import json

TOKEN = "XXXX:YYYYY" 
bot = telebot.TeleBot(TOKEN)

def getError():
  respuesta = "Algo salió mal con la API"
  return respuesta

def getBtc():
    try:
      response = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
      response = response.json()
      return str("{:,.2f}".format(float(response["last"])))
    except:
      return getError()

@bot.message_handler(commands=['panas1'])
def sentMessage(message):
    try:
      mensaje = 'Hola, '+'El precio del BTC es de: $' + getBtc()
    except:
      mensaje = 'Estoy agarrando señal carnal...'
    bot.reply_to(message, mensaje)

@bot.message_handler(commands=['panas2'])
def sentMessage(message):
    try:
      mensaje = 'La gata vestida de rata'
    except:
      mensaje = 'Estoy agarrando señal carnal...'
    bot.reply_to(message, mensaje)



bot.infinity_polling(timeout=10, long_polling_timeout = 5)
user = bot.get_me()
updates = bot.get_updates()
