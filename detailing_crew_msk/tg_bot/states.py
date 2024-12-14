from aiogram.filters import StateFilter
from aiogram.filters.state import State, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup


class ActionState(StatesGroup):
    action = State()


class AppointmentStates(StatesGroup):
    phone_num = State()
    name = State()
    choice_auto = State()
    desired_time = State()
    description = State()


class ReviewStates(StatesGroup):
    review = State()
    score = State()
    description = State()
