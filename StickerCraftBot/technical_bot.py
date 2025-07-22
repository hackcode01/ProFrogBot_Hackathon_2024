import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7175156175:AAGhdslcpg91uMSmTssBUcYxdTr5Yoy42MA"
ADMIN_ID = "942850147"

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

# Команда /start
@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Здравствуйте! Отправьте ваш вопрос или сообщение. Мы обработаем его в кратчайшие сроки.")

# Команда /return_bot
@dispatcher.message_handler(commands=["return_bot"])
async def message_support(message: types.Message):
    await message.reply("Перейдите по этой ссылке, чтобы вернуться к боту по созданию стикеров!")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Вернуться к боту", url="https://t.me/sticker_pro_frog_bot"))

    await message.reply("Нажмите кнопку, чтобы вернуться к боту:", reply_markup=keyboard)

# Команда /help
@dispatcher.message_handler(commands=["help"])
async def show_help(message: types.Message):
    commands = "Список команд:\n" \
                "/start - запустить бота\n" \
                "/return_bot - вернуться к боту по созданию стикеров\n" \
                "/help - помощь"

    await message.answer(commands)

# Ответ бота на входящие сообщения
@dispatcher.message_handler(lambda message: message)
async def handle_message(message: types.Message):
    if message != ("/return_bot" or "/start" or "/help"):
        await message.answer("Спасибо за ваше сообщение! Мы ответим вам в ближайшее время.")

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
