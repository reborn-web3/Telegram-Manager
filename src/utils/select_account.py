import os
from src.utils.db.utils_db import get_accounts


async def select_account(conn):
    accounts = await get_accounts(conn)

    if not accounts:
        print("Нет сохранённых аккаунтов.")
        return None

    print("\nВыберите аккаунт:")
    for idx, acc in enumerate(accounts, start=1):
        print(f"{idx}. {acc[1]} | Телефон: {acc[4]}")  # acc[1] = username, acc[4] = phone

    try:
        choice = int(input("Введите номер аккаунта: "))
        if 1 <= choice <= len(accounts):
            return accounts[choice - 1]
        else:
            print("Неверный выбор.")
            return None
    except ValueError:
        print("Введите корректное число.")
        return None
