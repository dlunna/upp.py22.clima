#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import requests
import json
import os
import subprocess

API_TOKEN = 'XXXX:YYYYY'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
      Hola !! soy solo un Bot, un Bot y nada mas. \
      /temp \
      Si tienes dudas contacta a dL o marcot.\
""")



def getBtc():
    try:
      response = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
      response = response.json()
      return str("{:,.2f}".format(float(response["last"])))
    except:
      return getError()

def temperatura():
    try:
      #response = os.system('ls')
      
      timevar = subprocess.check_output('sensors')
      #print ('la temperatura es:' + timevar)
      return str(timevar)
    except:
      return getError()


@bot.message_handler(commands=['crypto'])
def sentMessage(message):
    try:
      mensaje = 'Hola, '+'El precio del BTC es de: $' + getBtc()
    except:
      mensaje = 'Falla en la señal ...'
    bot.reply_to(message, mensaje)

@bot.message_handler(commands=['temp'])
def sentMessage(message):
    try:
      mensaje = 'La temperatura es:' + temperatura()
    except:
      mensaje = 'Falla en la señal ...'
    bot.reply_to(message, mensaje)






# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
