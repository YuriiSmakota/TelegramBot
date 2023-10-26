from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

base_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="CallBack Data", callback_data="CallBack Data"),
            InlineKeyboardButton(text="Google", url="https://google.com"),
        ],
        [
            InlineKeyboardButton(text="Switch Inline Query", switch_inline_query="Telegram"),
            InlineKeyboardButton(text="Switch Inline Query Current Chat", switch_inline_query_current_chat="Telegram")
        ]
    ]
)
