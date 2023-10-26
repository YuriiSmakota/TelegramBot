from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser

base_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Text 1"),
        ],
        [
            KeyboardButton(text="Text 2"),
            KeyboardButton(text="Text 3"),

        ],
        [
            KeyboardButton(text="Get Geo", request_location=True),
            KeyboardButton(text="Get Contact", request_contact=True),
            KeyboardButton(text="Get User", request_user=KeyboardButtonRequestUser(request_id=1)),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Reply Keyboard Input",
)
