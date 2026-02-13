from aiogram.fsm.state import State, StatesGroup


class InstagramLink(StatesGroup):
    user_link = State()