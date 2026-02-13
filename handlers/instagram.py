import os

from aiogram import Router, types, F
from states.instagram_state import InstagramLink
from aiogram.fsm.context import FSMContext

from aiogram.types import FSInputFile

from service.instagram_api import download_instagram_video

router = Router()


@router.message(F.text == "📸 Instagram")
async def instagram_handler(message: types.Message, state: FSMContext):
    await message.reply("Instagram havolasini yuboring")
    # await state.set_state(InstagramLink.user_link)



@router.message(F.text.startswith("http"))
async def get_instagram_url(message: types.Message):
    url = message.text

    if "instagram.com" not in url:
        await message.answer("❌ Bu Instagram havola emas")
        return

    msg = await message.answer("⏳ Video yuklanmoqda, kuting...")

    try:
        video_path = download_instagram_video(url)

        video = FSInputFile(video_path)
        await message.answer_video(video)

        # Faylni o‘chirish (ixtiyoriy, tavsiya qilaman)
        os.remove(video_path)

    except Exception as e:
        await message.answer("❌ Video yuklab bo'lmadi")
        print(e)

    await msg.delete()