from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = {
    "name": "@StickerCraft Bot",
    "token": "7168902691:AAHVXb7VQk-YNWIccx5CckvyhlI3XWGvrGE",
    "support_bot_token": "7175156175:AAGhdslcpg91uMSmTssBUcYxdTr5Yoy42MA",
    "mongoClient": "mongodb+srv://isfreak:isfreakMongoDB@cluster0.zjb8j91.mongodb.net/",
    "dbClient": "stickerpacks",
    "dbCollection": "photos",
}

bot = Bot(config["token"])
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

support_bot = Bot(config["support_bot_token"])
support_bot_storage = MemoryStorage()
support_bot_dispatcher = Dispatcher(support_bot, storage=support_bot_storage)
