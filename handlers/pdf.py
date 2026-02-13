# handlers/pdf.py

import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from service.pdf_api import create_pdf

router = Router()


class PdfState(StatesGroup):
    waiting_name = State()
    waiting_title = State()
    waiting_content = State()


@router.message(Command("pdf"))
async def start_pdf(message: Message, state: FSMContext):
    await message.answer("PDF nomini kiriting:")
    await state.set_state(PdfState.waiting_name)


@router.message(PdfState.waiting_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(file_name=message.text.strip())
    await message.answer("PDF sarlavhasini kiriting:")
    await state.set_state(PdfState.waiting_title)


@router.message(PdfState.waiting_title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text.strip())
    await message.answer("Matn yoki rasm yuboring.\nTayyor bo‘lsa PDF tayyorla deb yozing.")
    await state.set_state(PdfState.waiting_content)


@router.message(PdfState.waiting_content, F.text)
async def get_text(message: Message, state: FSMContext):

    if message.text.lower() == "pdf tayyorla":

        data = await state.get_data()

        file_name = data["file_name"]
        title = data["title"]
        content_list = data.get("content", [])

        pdf_file = create_pdf(file_name, title, content_list)

        await message.answer_document(FSInputFile(pdf_file))
        await message.answer("<b>PDF tayyorlandi ✅</b>", parse_mode="HTML")

        os.remove(pdf_file)
        await state.clear()
        return

    data = await state.get_data()
    content_list = data.get("content", [])
    content_list.append({"type": "text", "data": message.text})
    await state.update_data(content=content_list)


@router.message(PdfState.waiting_content, F.photo)
async def get_photo(message: Message, state: FSMContext):

    photo = message.photo[-1]
    file = await message.bot.get_file(photo.file_id)
    downloaded = await message.bot.download_file(file.file_path)

    image_name = f"{photo.file_id}.jpg"

    with open(image_name, "wb") as f:
        f.write(downloaded.read())

    data = await state.get_data()
    content_list = data.get("content", [])
    content_list.append({"type": "image", "data": image_name})
    await state.update_data(content=content_list)
