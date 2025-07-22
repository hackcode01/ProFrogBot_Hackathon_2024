from configure import Dispatcher, dispatcher

from functions import types
from functions import send_photos_сomputer_technology
from functions import send_photos_emotions_and_expressions
from functions import send_photos_phrases_and_memes

import logging

from aiogram import executor

logging.basicConfig(level=logging.INFO)

# Команда /start
@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(f"Привет, {message.from_user.full_name}! " +
                        "Я бот) Добро пожаловать!")

# Загрузка фотографий
@dispatcher.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]

    await photo.download()
    await message.answer("Фотография сохранена!")

# Команда /choose_theme
@dispatcher.message_handler(commands=["choose_theme"])
async def choose_theme(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    keyboard.add(types.KeyboardButton(text="Компьютерные технологии"))
    keyboard.add(types.KeyboardButton(text="Эмоции и выражения"))
    keyboard.add(types.KeyboardButton(text="Фразы и мемы"))

    await message.reply("Выберите тему для стикерпака:", reply_markup=keyboard)

    if message.text == "Компьютерные технологии":
        await send_photos_сomputer_technology(message)
    elif message.text == "Эмоции и выражения":
        await send_photos_emotions_and_expressions(message)
    elif message.text == "Фразы и мемы":
        await send_photos_phrases_and_memes(message)

# Команда /source_code
@dispatcher.message_handler(commands=["source_code"])
async def source_code(message: types.Message):
    await message.reply("Исходный код доступен по ссылке:\n"
                        "https://github.com/AndreyRazin007/ProFrog_Hackathon_2024")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Перейти на GitHub", url="https://github.com/AndreyRazin007/ProFrog_Hackathon_2024"))

    await message.reply("Нажмите кнопку, чтобы перейти на GitHub:", reply_markup=keyboard)

# Команда /support
@dispatcher.message_handler(commands=["support"])
async def message_support(message: types.Message):
    await message.reply("Перейдите по этой ссылке, чтобы отправить сообщение в техническую поддержку!")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Отправить сообщение в техническую поддержку", url="https://t.me/ProFrogSupportBot"))

    await message.reply("Нажмите кнопку, чтобы отправить сообщение в техническую поддержку:", reply_markup=keyboard)

# Команда /help
@dispatcher.message_handler(commands=["help"])
async def show_help(message: types.Message):
    commands = "Список команд:\n" \
                "/start - запустить бота\n" \
                "/choose_theme - выбрать тему для стикерпака\n" \
                "/source_code - вывести ссылку на исходный код\n" \
                "/support - отправить сообщение в техническую поддержку\n" \
                "/help - помощь"

    await message.answer(commands)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == "__main__":
    executor.start_polling(dispatcher, on_shutdown=shutdown, skip_updates=True)
