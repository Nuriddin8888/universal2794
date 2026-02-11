from aiogram import Bot, Dispatcher, types, F
from aiogram.types import CallbackQuery
from gtts import gTTS
import io

from buttons.inline import language_keyboard
from service.translate_api import tarjimon

dp = Dispatcher()

@dp.message(F.text == "🌐Tarjima")
async def tarjima_start(message: types.Message):
    await message.answer("✍️ Tarjima qilmoqchi bo'lgan matnni yuboring")


@dp.message(F.text)
async def get_text(message: types.Message, state=None):
    text = message.text

    message.bot_data.setdefault(message.from_user.id, {})
    message.bot_data[message.from_user.id]["text"] = text

    await message.answer(
        "🌍 Qaysi tilga tarjima qilay?",
        reply_markup=language_keyboard(0)
    )


@dp.callback_query()
async def inline_handler(call: CallbackQuery):
    data = call.data
    user_id = call.from_user.id

    if data == "noop":
        await call.answer()
        return

    if data.startswith("page:"):
        page = int(data.split(":")[1])
        await call.message.edit_reply_markup(
            reply_markup=language_keyboard(page)
        )
        await call.answer()
        return

    if data.startswith("tts:"):
        lang = data.split(":")[1]

        user_text = call.bot.bot_data.get(user_id, {}).get("text")
        if not user_text:
            await call.message.edit_text("❌ Matn topilmadi")
            return

        translated = tarjimon(user_text, lang)

        await call.message.edit_text(
            f"🌐 Tarjima:\n\n{translated}"
        )

        mp3 = io.BytesIO()
        tts = gTTS(text=translated, lang=lang)
        tts.write_to_fp(mp3)
        mp3.seek(0)

        await call.message.answer_voice(mp3)
        await call.answer()
