# Импорт aiogram
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

# Импорт мои файлов
from resource import Keyboard
from resource import QrCode

# Импорт DotEnv и OS
from dotenv import load_dotenv
import os

load_dotenv() # Загрузка DotEnv
bot = Bot(os.getenv("TOKEN")) # Добавление токена
disp = Dispatcher(bot=bot) # Для управления ботом

# Команда Start
@disp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    first_name = message.from_user.first_name # Запись имени тг

    await message.answer(f"{first_name}, добро пожаловать 🖐️", reply_markup=Keyboard.user_keyb)
    await message.answer(
        f"{first_name}, если хотите следить за новостями подпишись на мой канал.",
        reply_markup=Keyboard.keyb_sub
    )

# Команда back
@disp.message_handler(commands=["back"])
async def back(message: types.Message):
    await message.answer("Вы вышли назад!", reply_markup=Keyboard.user_keyb)

# Обработчик сообщения (обрабатывает текст)
@disp.message_handler(text="Инструменты ⚒️")
async def tools(message: types.Message):
    first_name = message.from_user.first_name  # Запись имени тг

    await message.answer(
        f"{first_name}, выбери нужный инструмент из списка в меню 🧰",
        reply_markup=Keyboard.keyb_tools
    )
    await message.answer("Чтобы выйти из меню инструментов введите /back")

# Обработчик сообщения (обрабатывает текст)
@disp.message_handler(text="Информация 📃")
async def infos(message: types.Message):
    await message.answer(
        """
            Разработчик: @Zadvornow
GitHub: https://github.com/Skybicx
        """
    )

# Обработчик сообщения (обрабатывает текст)
@disp.message_handler(text="Поддержка 🆘")
async def infos(message: types.Message):
    await message.answer("Данный раздел находиться в разработке ):")

# Обработчик сообщения (обрабатывает текст)
@disp.message_handler(text="Создать QrCode")
async def create_qrcode(message: types.Message):
    first_name = message.from_user.first_name  # Запись имени тг
    await message.answer(f"{first_name}, введи данные которые надо записать в QrCode")

# Обработчик для создания QrCode
@disp.message_handler(content_types=["text"])
async def check_message(message: types.Message):
    await message.answer("Подгодовка файла...")
    if os.path.exists("qrcode.png") == False:
        QrCode.Create(message.text) # Создание qr-кода
        file = open("qrcode.png", 'rb') # Открытие qr-кода
        await message.answer("Отправка файла...")
        await message.answer_photo(photo=file)
        file.close() # Закрытие qr-кода
        os.remove("qrcode.png") # Удаление qr-кода
    else:
        os.remove("qrcode.png") # Удаление qr-кода
        QrCode.Create(message.text) # Создание qr-кода
        file = open("qrcode.png", 'rb') # Открытие qr-кода
        await message.answer("Отправка файла...")
        await message.answer_photo(photo=file)
        file.close() # Закрытие qr-кода
        os.remove("qrcode.png") # Удаление qr-кода

if __name__ == "__main__":
    executor.start_polling(disp, skip_updates=True)