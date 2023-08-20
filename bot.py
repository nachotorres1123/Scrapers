import requests
from bs4 import BeautifulSoup
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Configuración del bot
TOKEN = 6476747450:AAEY8OyxUcIYhbOXi2Ek_3DvbNhFIDSGbKk # Reemplaza 'TU_TOKEN_AQUÍ' con el token de tu bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Función para extraer datos de la página web
def extract_data():
    url = 'https://randomaddress-9d94ddea293c.herokuapp.com/'  # Cambia esta URL a la página de la que deseas extraer datos
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Aquí selecciona los elementos que deseas extraer usando métodos de BeautifulSoup

        # Ejemplo: Extraer el texto de todos los elementos <h1> en la página
        data = [element.text for element in soup.find_all('h1')]

        return data
    else:
        return None

# Manejador del comando /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("¡Hola! Soy un bot para extraer datos de una página web y mostrarlos en Telegram.")

# Manejador del comando /getdata
@dp.message_handler(commands=['getdata'])
async def get_data(message: types.Message):
    await message.answer_chat_action('typing')

    extracted_data = extract_data()
    if extracted_data:
        data_message = '\n'.join(extracted_data)
        await message.reply(data_message)
    else:
        await message.reply('No se pudo obtener los datos.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
