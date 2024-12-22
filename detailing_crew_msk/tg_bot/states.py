from aiogram.filters import StateFilter
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class ActionState(StatesGroup):
    action = State()
    # create_appointment = State()
    # create_review = State()


class AppointmentStates(StatesGroup):
    phone_num = State()
    name = State()
    desired_time = State()


class ReviewStates(StatesGroup):
    review = State()
    score = State()
    description = State()
