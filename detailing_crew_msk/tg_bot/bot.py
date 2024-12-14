import asyncio
import os
import logging
import sys

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold

from aiogram.filters import StateFilter
from aiogram.filters.state import State, StateFilter
from aiogram.fsm.context import FSMContext

from callbacks import MyCallback
from keyboards import start_keyboard, review_keyboard
from texts import GREETING_TEXT
from states import ActionState, AppointmentStates, ReviewStates

# Включаем логирование
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp = Dispatcher()
TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')


@dp.message(CommandStart())
# Отработчик команды "/start" с клавиатурой с двумя кнопками.
async def command_start_handler(message: Message, state: FSMContext):
    """
    This handler receives messages with `/start` command
    """
    await state.set_state(ActionState.action)
    await message.answer(
        text=GREETING_TEXT,
        reply_markup=start_keyboard(),
    )


# @dp.message(ActionState.action, ```ЧТО СЮДА ПИСАТЬ, ЧТОБЫ ВЫЦЕПИТЬ ДАННЫЕ ИЗ КНОПКИ?```)
@dp.callback_query(MyCallback.filter(F.data == 'appointment'))
# async def appointment_action(message: Message, state: FSMContext):
async def appointment_action(query: CallbackQuery,
                            #  message: Message,
                             callback_data: MyCallback,
                             state: FSMContext):
    await state.set_state(AppointmentStates.phone_num)
    await query.answer('Введите ваш номер телефона:', show_alert=True)

# # @dp.message_handler()
# # async def process_message(message: types.Message):
#     # Проверяем, что пользовательский ввод является номером телефона
#     if message.text.isdigit() and len(message.text) == 10:
#         # Валидация успешна, создаем кнопку "Подтвердить"
#         from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#         keyboard = InlineKeyboardMarkup()
#         keyboard.add(InlineKeyboardButton("Подтвердить", callback_data="confirm"))

#         await message.answer("Вы ввели номер телефона: " + message.text, reply_markup=keyboard)
#     else:
#         await message.answer("Пожалуйста, введите корректный номер телефона (10 цифр)")





async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TGBOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

def tg_bot():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())