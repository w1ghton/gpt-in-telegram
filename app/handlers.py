from aiogram import Router, types
from aiogram.filters.command import CommandStart

from ai import ai_answer

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("йоу")


@router.message()
async def to_ai(message: types.Message):
    user_query = message.text
    try:
        answer = await ai_answer(user_query, "gpt-4o-mini")
        await message.answer(answer, parse_mode="Markdown")
    except Exception as e:
        await message.reply("Произошла ошибка при обработке запроса.")
        print(f"Error: {e}")
