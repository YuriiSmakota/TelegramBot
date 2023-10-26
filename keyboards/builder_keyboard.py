from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="ONE")
    builder.button(text="TWO")
    builder.button(text="THREE")
    builder.button(text="FOUR")
    builder.button(text="FIVE")
    builder.button(text="SEX")
    builder.button(text="SEVEN")
    builder.button(text="EIGHT")
    builder.button(text="NINE")
    builder.button(text="TEN"),
    builder.adjust(1, 2, 3, 4)

    return builder.as_markup(resize_keyboard=True)


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="1", callback_data="1")
    builder.button(text="2", callback_data="2")
    builder.button(text="3", callback_data="3")
    builder.button(text="4", callback_data="4")
    builder.button(text="5", callback_data="5")
    builder.button(text="6", callback_data="7")
    builder.button(text="7", callback_data="7")
    builder.button(text="8", callback_data="8")
    builder.button(text="9", callback_data="9")
    builder.button(text="10", callback_data="10")
    builder.adjust(1, 2, 3, 4)
    return builder.as_markup()

# from keyboards.builder_keyboard import get_reply_keyboard
