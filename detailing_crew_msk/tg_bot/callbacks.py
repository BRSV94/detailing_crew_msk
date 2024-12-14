from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix='my'):
    data: str


appointment_callback = MyCallback(data='appointment').pack()
review_callback = MyCallback(data='review').pack()
