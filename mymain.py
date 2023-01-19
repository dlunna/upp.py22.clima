from tkinter import Scale
from aiogram import Bot, Dispatcher, executor, types
import pyqrcode

bot = Bot(token='5961465534:AAFUxL9xF8ZwxaTBGFE28r_WDrIyC7IELC4')
db = Dispatcher(bot)

@db.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("""\
      Hola !! bienvenida, bienvenido \
      Encuentro Hidalguense de Investigadores SNI \
      30 de Enero del 2023 \
      https://ijse.com.mx\

""")

@db.message_handler(commands=['help'])
async def welcome(message: types.Message):
    await message.reply("""\
      Comandos disponibles:\
      start \
      help \
      programa \
\
""")

@db.message_handler(commands=['programa'])
async def logo(message: types.Message):
    await message.answer_photo('https://www.upp.edu.mx/main/images/slider/banner_100_dias.jpg')

#@db.message_handler()
#async def echo(message: types.Message):
#    await message.answer(message.text)

@db.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))

executor.start_polling(db)