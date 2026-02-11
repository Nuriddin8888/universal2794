from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Instagram")],

        [
            KeyboardButton(text="🕌 Namoz vaqti"),
            KeyboardButton(text="🤖 ChatGPT")
        ],
        [KeyboardButton(text="📄 PDF")],

        [
            KeyboardButton(text="🌐 Tarjima"),
            KeyboardButton(text="⛅️ Ob-havo")
        ]
    ],
    resize_keyboard=True
)