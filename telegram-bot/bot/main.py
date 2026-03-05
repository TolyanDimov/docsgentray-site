import asyncio
import httpx
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = 'CHANGE_ME'
    api_base_url: str = 'http://backend:8000'
    bot_api_token: str = 'change-bot-api-token'


settings = Settings()
bot = Bot(token=settings.bot_token)
dp = Dispatcher()


def _headers() -> dict[str, str]:
    return {'x-bot-token': settings.bot_api_token}


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Добро пожаловать в DocsGenTray bot. Команды: /license <email> и /renew')


@dp.message(Command('license'))
async def license_status(message: Message):
    parts = message.text.split(maxsplit=1) if message.text else []
    if len(parts) < 2:
        await message.answer('Использование: /license you@example.com')
        return

    email = parts[1].strip()
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f'{settings.api_base_url}/bot/license/{email}', headers=_headers())

    if response.status_code == 200:
        data = response.json()
        await message.answer(
            f"Лицензия:\nEmail: {data['email']}\nТариф: {data['tariff']}\n"
            f"Срок: {data['expires_at']}\nСтатус: {data['status']}"
        )
    elif response.status_code == 404:
        await message.answer('Пользователь не найден')
    else:
        await message.answer('Сервис временно недоступен')


@dp.message(Command('renew'))
async def renew(message: Message):
    await message.answer('Заявка на продление принята. Менеджер свяжется с вами.')


@dp.message(F.text)
async def fallback(message: Message):
    await message.answer('Неизвестная команда. Используйте /license <email> или /renew')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
