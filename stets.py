from aiogram.fsm.state import State, StatesGroup
class Form(StatesGroup):
    kasb = State()
    name = State()
    phone = State()
    lacation = State()
    admin = State()

