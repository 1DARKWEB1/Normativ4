import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API_TOKEN = '8199528786:AAGNvFfO_r8zgdWNSZQi3gmV1GpdrYpNRMQ'
API_URL = 'http://127.0.0.1:8000/api/courses/'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# 🔹 Получаем курсы из Django API
async def get_courses(params: str = ""):
    url = f"{API_URL}?{params}" if params else API_URL
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# 🔹 Старт — показываем список всех курсов
@dp.message(Command("start"))
async def start(message: types.Message):
    courses = await get_courses()
    if not courses:
        await message.answer("❌ Курсы не найдены.")
        return

    text = "📚 *Доступные курсы:*\n\n"
    for c in courses:
        text += f"• {c['title']} (ID: {c['id']})\n"
    text += (
        "\n🔎 Чтобы найти курс:\n"
        "— просто введите *номер ID* (например: 2)\n"
        "— или часть названия (например: python)"
    )

    await message.answer(text, parse_mode="Markdown")


# 🔹 Обрабатываем ввод пользователя
@dp.message()
async def handle_filter(message: types.Message):
    query = message.text.strip()

    # Если пользователь ввёл число — фильтруем по ID
    if query.isdigit():
        param = f"id__gte={query}"
    else:
        # Если текст — ищем по названию
        param = f"title__icontains={query}"

    data = await get_courses(param)

    if not data:
        await message.answer("⚠️ Ничего не найдено по вашему запросу.")
        return

    text = "🎯 *Результаты поиска:*\n\n"
    for c in data:
        text += f"🏷 *{c['title']}*\n{c['description']}\n\n"

    await message.answer(text, parse_mode="Markdown")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
