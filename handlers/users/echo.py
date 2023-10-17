from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    file_id=message.document.file_id
    await message.answer(text=f"{file_id}")
