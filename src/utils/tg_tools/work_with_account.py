import os

from src.config import SESSIONS_DIR

from src.utils.tg_tools.tools import Account, ChangeAccount, Channel

async def work_with_account(account):
    _, username, api_id, api_hash, phone = account
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print("        Telegram Account Manager      ")
        print("======================================")
        print("\nВыбранный аккаунт:")
        print(f'@{username}: {phone}')
        print("Выберите действие:")
        print("1. Изменение аккаунта")
        print("2. Каналы")
        print("3. Scrapper")
        print("4. Gifts autobuy")
        print("5. Выход в меню")
        
        try:
            choice = int(input("\nВыберите опцию: "))
        except ValueError:
            print("Пожалуйста, введите число.")
            continue
        if choice == 1:
            await create_change_accout_menu(username, api_id, api_hash, phone)
            
        elif choice == 2:
            break

        elif choice == 3:
            break
        
        elif choice == 4:
            break

        elif choice == 5:
            break

        else: print("Неверный выбор. Пожалуйста, попробуйте снова.")


async def create_change_accout_menu(username, api_id, api_hash, phone):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выберите действие:")
        print("1. Изменить юзернейм")
        print("2. Изменить никнейм")
        print("3. Изменить био")
        print("4. Изменить аватар")
        print("5. Юзернейм чекер")
        print("6. Выход")

        try:
            choice = int(input("\nВыберите опцию: "))
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        if choice == 1:
            new_username = input("Введите новый юзернейм: ")
            
            account = Account(username, api_id, api_hash, phone)
            change_account = ChangeAccount(account)
            
            await change_account.change_username(new_username)
            
            input(f'Никнейм {new_username} поставлен')

        elif choice == 2:
            new_nickname = input("Введите новый ник: ")
            
            account = Account(username, api_id, api_hash, phone)
            change_account = ChangeAccount(account)
            await change_account.change_nickname(new_nickname)

            input(f'Никнейм {new_nickname} поставлен')

        elif choice == 3:
            new_bio = input("Введите новое био: ")

            account = Account(username, api_id, api_hash, phone)
            change_account = ChangeAccount(account)
            await change_account.change_bio(new_bio)

            input(f'\nНовое био {new_bio} поставлено. Нажмите enter для продолжения...')

        elif choice == 4:
            account = Account(username, api_id, api_hash, phone)
            change_account = ChangeAccount(account)
            
            print('Not yet created')

        elif choice == 5:
            account = Account(username, api_id, api_hash, phone)
            change_account = ChangeAccount(account)

            available_usernames = await change_account.username_checker()

            input(f'\nДоступные юзернеймы: {available_usernames} поставлено. Нажмите enter для продолжения...')

        elif choice == 6:
            break
        
        else: print("Неверный выбор. Пожалуйста, попробуйте снова.")


async def create_channel_menu(username, api_id, api_hash, phone):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выберите действие:")
        print("1. Изменить юзернейм")
        print("2. Изменить никнейм")
        print("3. Изменить био")
        print("4. Изменить аватар")
        print("5. ВЫход")
        

