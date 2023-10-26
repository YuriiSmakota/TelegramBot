from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text="ONE")
    keyboard_builder.button(text="TWO")
    keyboard_builder.button(text="THREE")
    keyboard_builder.button(text="FOUR")
    keyboard_builder.button(text="FIVE")
    keyboard_builder.button(text="SEX")
    keyboard_builder.button(text="SEVEN")
    keyboard_builder.button(text="EIGHT")
    keyboard_builder.button(text="NINE")
    keyboard_builder.button(text="TEN"),

    keyboard_builder.adjust(1, 2, 3, 4),
    return keyboard_builder.as_markup()


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="1", callback_data="1")
    keyboard_builder.button(text="2", callback_data="2")
    keyboard_builder.button(text="3", callback_data="3")
    keyboard_builder.button(text="4", callback_data="4")
    keyboard_builder.button(text="5", callback_data="5")
    keyboard_builder.button(text="6", callback_data="7")
    keyboard_builder.button(text="7", callback_data="7")
    keyboard_builder.button(text="8", callback_data="8")
    keyboard_builder.button(text="9", callback_data="9")
    keyboard_builder.button(text="10", callback_data="10")

    keyboard_builder.adjust(1, 2, 3, 4)
    return keyboard_builder.as_markup()


