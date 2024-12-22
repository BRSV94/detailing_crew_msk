import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detailing_crew_msk.settings')
django.setup()

import asyncio
import os
import logging
import re
import sys

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv

from callbacks import MyCallback
from keyboards import start_keyboard, review_keyboard
from texts import GREETING_TEXT
from states import AppointmentStates, ReviewStates

from detailing.models import AppointmentThroughTg

# Включаем логирование
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# dp = Dispatcher()
r = Router()
load_dotenv()
TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')


@r.message(CommandStart())
# Отработчик команды "/start" с клавиатурой с двумя кнопками.
async def command_start_handler(message: Message):
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        text=GREETING_TEXT,
        reply_markup=start_keyboard(),
    )


@r.callback_query(MyCallback.filter(F.data == 'appointment'))
# @r.message(ActionState.action, F.text.casefold() == "appointment")
async def create_appointment(message: Message, state: FSMContext):

    await state.set_state(AppointmentStates.phone_num)
    await message.answer(
        'Введите ваш номер телефона:',
        show_alert=False,
    )


@r.message(AppointmentStates.phone_num)
async def add_phone_number(message: Message, state: FSMContext):
    pattern = re.compile(r'^(\+7|8)\d{10}$')
    if bool(pattern.match(message.text)):
        await state.update_data(phone_num=message.text)
        await state.set_state(AppointmentStates.name)
        await message.answer("Как к Вам можно обратиться?")
    else:
        await message.answer(
            'Введите корректный номер телефона в формате '
            '+7XXXXXXXXXX или 8XXXXXXXXXX.')
        

@r.message(AppointmentStates.name)
async def add_client_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text.title())
    await state.set_state(AppointmentStates.desired_time)
    await message.answer(
        "Когда вам можно позвонить и уточнить данные по записи?"
    )


@r.message(AppointmentStates.desired_time)
async def create_appointment(message: Message, state: FSMContext):
    data = await state.update_data(desired_time=message.text)
    phone_num = data.get('phone_num')
    name = data.get('name')
    desired_time = data.get('desired_time')
    appointment = AppointmentThroughTg(
        phone_number=phone_num,
        name=name,
        desired_time=desired_time,
    )
    await message.answer(
        f'{name}, благодарим за обращение.\n'
        'Наш администратор позвонит вам для уточнения информации по записи '
        f'на номер: {phone_num}.'
    )
    # appointment.save()
    # appointment = (
    #     f'Тел.: {phone_num}\n'
    #     f'Имя: {name}\n'
    #     f'Когда звонить: {desired_time}'
    # )
    # await message.answer(appointment)


# @r.callback_query(MyCallback.filter(F.data == 'review'))
# async def create_appointment(message: Message, state: FSMContext):
#     # await state.set_data(AppointmentStates.phone_num)
#     await message.answer(
#         'Напишите отзыв.',
#         show_alert=False,
#     )


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TGBOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(r)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

def tg_bot():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())