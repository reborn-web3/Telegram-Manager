import logging
import os

from .conn_db import get_connection
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


async def add_account(conn):
    os.makedirs("sessions", exist_ok=True)

    try:
        api_id = input('Введи api_id: ').strip()
        api_hash = input('Введи api_hash: ').strip()
        phone = input('Введи номер телефона (просто 11 цифр, без плюса): ').strip()

        if not (api_id and api_hash and phone):
            raise ValueError("Все поля должны быть заполнены.")

        client = TelegramClient(f'sessions/{phone}_session', api_id, api_hash)
        await client.connect()

        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            try:
                await client.sign_in(phone, input('Введите код: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Введите пароль: '))

        user = await client.get_me()
        username = user.username if user.username else str(user.id)
        
        await add_account_to_db(conn,username, api_id, api_hash, phone)
        logging.info(f"Аккаунт {username} добавлен.")
        account = (username, api_id, api_hash, phone)

        await client.disconnect()
        return account
    except Exception as e:
        print(f"Ошибка: {e}")
 
async def add_account_to_db(conn, username, api_id, api_hash, phone):
    await conn.execute(
        "INSERT INTO accounts (username, api_id, api_hash, phone) VALUES (?, ?, ?, ?)",
        (username, api_id, api_hash, phone)
    )
    await conn.commit()


async def get_accounts(conn):
    async with conn.execute("SELECT * FROM accounts") as cursor:
        rows = await cursor.fetchall()
        return rows
    
