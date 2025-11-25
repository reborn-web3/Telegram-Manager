import os
import asyncio

from src.utils.db.conn_db import *
from src.utils.db.utils_db import *
from src.utils.select_account import select_account
from src.utils.tg_tools.work_with_account import work_with_account



async def create_menu():
    conn = await get_connection()
    selected_account = None
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print("        Telegram Account Manager      ")
        print("======================================")
        print("\nГлавное меню:")
        print("1. Добавить новый аккаунт")
        print("2. Показать все аккаунты")
        print("3. Выбрать аккаунт")
        print("4. Работа с аккаунтом")
        print("5. Выход")
        
        try:
            choice = int(input("\nВыберите опцию: "))
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        if choice == 1:
            await add_account(conn)
        
        elif choice == 2:
            accounts = await get_accounts(conn)
            for account in accounts:
                print(account)
            input('\n\n\nНажмите enter чтобы продолжить...')
        
        elif choice == 3:
            selected_account = await select_account(conn)
            if selected_account:
                print(f"✅ Выбран аккаунт: {selected_account[1]}")
            else:
                print("❌ Не удалось выбрать аккаунт.")
            input("Нажмите Enter для продолжения...")
            
        elif choice == 4:
            if not selected_account:
                print("⚠️ Сначала выберите аккаунт (опция 3).")
                input("\nНажмите Enter для продолжения...")
            else:
                await work_with_account(selected_account)
            

        elif choice == 5:
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
    
    await conn.close() 
