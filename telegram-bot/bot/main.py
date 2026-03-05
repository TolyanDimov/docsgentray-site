import asyncio
import httpx
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = 'CHANGE_ME'
    api_base_url: str = 'http://backend:8000'


settings = Settings()
bot = Bot(token=settings.bot_token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Добро пожаловать в DocsGenTray bot. Команды: /license /renew')


@dp.message(Command('license'))
async def license_status(message: Message):
    await message.answer('Отправьте email в формате: email you@example.com')


@dp.message(F.text.startswith('email '))
async def lookup(message: Message):
    email = message.text.replace('email ', '').strip()
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f'{settings.api_base_url}/admin/users')
    if response.is_success:
        await message.answer(f'Запрос по {email} принят. Свяжитесь с поддержкой для детального статуса лицензии.')
    else:
        await message.answer('Сервис временно недоступен')


@dp.message(Command('renew'))
async def renew(message: Message):
    await message.answer('Заявка на продление принята. Менеджер свяжется с вами.')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
