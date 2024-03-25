from aiogram.types import FSInputFile

# import led
# import camera_bot
# import DHT

import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.environ.get('BOT_TOKEN'))
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("led_on"))
async def cmd_start(message: types.Message):
    # led.led_on()
    await message.answer("Светодиод включен")


@dp.message(Command("led_off"))
async def cmd_start(message: types.Message):
    # led.led_off()
    await message.answer("Светодиод выключен")


@dp.message(Command("make_photo"))
async def cmd_start(message: types.Message):
    # camera_bot.make_photo()
    photo = FSInputFile("test.jpg")
    await message.answer_photo(photo=photo)
    await message.answer("Фото сделано")


@dp.message(Command("get_temperature"))
async def cmd_start(message: types.Message):
    # hum, tem = DHT.get_value()
    hum, tem = 51, 23
    await message.answer(f"Температура: {tem} ℃\nВлажность: {hum} %")


@dp.message(Command("help"))
async def commands(message: types.Message):
    commands = {'/start': 'Нажмите для запуска бота',
                '/help': 'Нажмите для просмотра доступных команд',
                '/led_on': 'Включить светодиод',
                '/led_off': 'Выключить светодиод',
                '/make_photo': 'Сделать снимок с камере Raspberry',
                '/get_temperature': 'Вывести значение темепературы и влажности с датчика'
                }
    for command, discription in commands.items():
        await message.answer(f'{command}\n{discription}')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
