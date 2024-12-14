from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove)
from callbacks import appointment_callback, review_callback


def start_keyboard():
    # keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    appointment_button = InlineKeyboardButton(
        text='Записаться',
        callback_data=appointment_callback,
    )
    review_button = InlineKeyboardButton(
        text='Оставить отзыв',
        callback_data=review_callback,
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [appointment_button],
            [review_button],
        ],
    )

    # keyboard.add(sign_up_button)
    # keyboard.add(review_button)

    return keyboard

def review_keyboard():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    GREAT = 5, 'Отлично'
    WELL = 4, 'Хорошо'
    MEDIUM = 3, 'Средне'
    BAD = 2, 'Плохо'
    WTF = 1, 'Ужасно'
    great = InlineKeyboardButton(
        text='Отлично',
        callback_data='great'
    )
    well = InlineKeyboardButton(
        text='Хорошо',
        callback_data='well'
    )
    medium = InlineKeyboardButton(
        text='Средне',
        callback_data='medium'
    )
    bad = InlineKeyboardButton(
        text='Плохо',
        callback_data='bad'
    )
    wtf = InlineKeyboardButton(
        text='Ужасно',
        callback_data='wtf'
    )
    keyboard.add(great)
    keyboard.add(well)
    keyboard.add(medium)
    keyboard.add(bad)
    keyboard.add(wtf)

    return keyboard



    