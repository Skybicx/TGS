from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

# Пользовательская клавиатура
user_keyb = ReplyKeyboardMarkup(resize_keyboard=True)
user_keyb.add("Инструменты ⚒️")
user_keyb.add("Информация 📃")
user_keyb.add("Поддержка 🆘")

# Клавиатура для подписки на канал
keyb_sub = InlineKeyboardMarkup(row_width=1)
keyb_sub.add(
    InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/skybicx"),
    InlineKeyboardButton(text="Подписаться на YouTube", url="http://www.youtube.com/@Skybicx")
)

keyb_tools = ReplyKeyboardMarkup(resize_keyboard=True)
keyb_tools.add("Создать QrCode")