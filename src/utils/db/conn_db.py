import asyncio
import os
import aiosqlite
from datetime import datetime

# Получаем абсолютный путь к файлу базы данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'accounts.db')  # База в той же папке, что и conn_db.py

async def get_connection():
    return await aiosqlite.connect(DB_PATH)

async def init_db():
    async with await get_connection() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT DEFAULT NULL,
            api_id TEXT NOT NULL,
            api_hash TEXT NOT NULL, 
            phone TEXT NOT NULL
        )
        """)
        await conn.commit()

# async def edit_db():
#     conn = await get_connection()
#     await conn.execute("""
#         UPDATE accounts 
#         SET api_id = ?, api_hash = ?, phone = ?
#         WHERE id = 1
#     """, ('None', 'None', 'None'))
#     await conn.commit()
#     await conn.close()

# asyncio.run(edit_db())