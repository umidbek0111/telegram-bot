from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ustoz kerak")]
    ],
    resize_keyboard=True
)


phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="yuborish ☎ ", request_contact=True)]
    ],
    resize_keyboard=True
)

confirm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="HA"), KeyboardButton(text='YOQ')]
    ],
    resize_keyboard=True
)