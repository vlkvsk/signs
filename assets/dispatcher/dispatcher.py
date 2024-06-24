from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import assets.config.cfg as config

config_variables = {
    "BOT_TOKEN": config.BOT_TOKEN,
    "a_chat_id": config.a_chat_id,
    "model_id": config.model_id,
}

missing_variables = [k for k, v in config_variables.items() if not v]
if missing_variables:
    exit(f"Отсутствуют конфигурационные переменные: {', '.join(missing_variables)}")

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

print("Бот успешно запущен.")