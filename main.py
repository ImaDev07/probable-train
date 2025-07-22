# 1.Aiogram

# 1 вопрос.
# Aiogram — это современная асинхронная библиотека Python для разработки Telegram-ботов
# Преимущества Aiogram:
# 1. Асинхронность: использует asyncio, что обеспечивает высокую скорость обработки сообщений
# 2.FSM: удобно управлять диалогами и состояниями пользователя
# 3. Возможности API Telegram: отправка сообщений, клавиатур, медиа, и мн.др.
# 4. Обработка команд и сообщений

# 2 вопрос.
# Bot- основной объект, который взаимодействует с Telegram API, отправляет и получает сообщения
# Dispatcher- маршрутизатор входящих сообщений и команд. Также связывает их с соответствующими хэндлерами
# Хэндлеры- функции, которые реагируют на определенные действия, например, команду /start, текстовые сообщения и тд.
# FSM- механизм управления состояниями диалога, помогает реализовать многошаговые взаимодействия с пользователем




#Практика.
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Привет")
    keyboard.add("Пока")
    await message.answer("Выберите команду:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Привет")
async def say_hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message_handler(lambda message: message.text == "Пока")
async def say_bye(message: types.Message):
    await message.answer("До свидания!")

if __name__ == '__main__':
    executor.start_polling(dp)






