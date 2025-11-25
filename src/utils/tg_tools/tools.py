import asyncio
import os
import random

from src.config import SESSIONS_DIR
from telethon import TelegramClient, functions, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateUsernameRequest, CheckUsernameRequest
from telethon.errors import SessionPasswordNeededError, UsernameInvalidError, UsernameOccupiedError, AboutTooLongError, FirstNameInvalidError


class Account:
    def __init__(self, username, api_id, api_hash, phone):
        self.username = username
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone

        

class ChangeAccount:
    def __init__(self, account: Account):
        self.account = account

    async def _get_client(self) -> TelegramClient:
        session_path = os.path.join(SESSIONS_DIR, f"{self.account.phone}_session")
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        client = TelegramClient(session_path, self.account.api_id, self.account.api_hash)
        await client.connect()
        return client
    
    async def change_nickname(self, new_username: str):
        try:
            async with await self._get_client() as client:
                await client(functions.account.UpdateProfileRequest(
                    first_name= new_username,
                ))
                
        except (AboutTooLongError, FirstNameInvalidError) as e:
            print(e)
        

    async def change_bio(self, about):
        try:
            async with await self._get_client() as client:
                await client(functions.account.UpdateProfileRequest(
                    about= about,
                ))
                
        except (AboutTooLongError, FirstNameInvalidError) as e:
            print(e)

    async def change_avatar(self, file_path: str):
        if not os.path.isfile(file_path):
            print(f"Файл {file_path} не найден.")
            return

        try:
            async with await self._get_client() as client:
                file = await client.upload_file(file_path)
                await client(UploadProfilePhotoRequest(file))
                print("✅ Аватар успешно изменён.")
        except Exception as e:
            print(f"❌ Ошибка при смене аватара: {e}") 





    async def change_username(self, new_username: str):
        try:
            async with await self._get_client() as client:
                # Проверяем доступность имени
                is_available = await client(CheckUsernameRequest(new_username))
                if not is_available:
                    print(f"❌ Имя пользователя @{new_username} уже занято.")
                    return

                # Устанавливаем юзернейм
                await client(UpdateUsernameRequest(new_username))
                print(f"✅ Юзернейм успешно изменён на: @{new_username}")

        except UsernameInvalidError:
            print("❌ Некорректное имя пользователя.")
        except UsernameOccupiedError:
            print("❌ Это имя пользователя уже занято.")
        except SessionPasswordNeededError:
            print("❌ Требуется пароль двухфакторной аутентификации.")
        except Exception as e:
            print(f"❌ Неизвестная ошибка: {e}")

    
    async def username_checker(self):
        available = []

        async with await self._get_client() as client:
            with open('src/utils/tg_tools/username/usernames.txt', 'r', encoding='utf-8') as usernames:
                for username in usernames:
                    username = username.strip()
                    if not username:
                        continue  # пропускаем пустые строки
                    
                    try:
                        is_available = await client(CheckUsernameRequest(username))
                        if is_available:
                            print(f"✅ Доступен: @{username}")
                            available.append(username)
                            # Можно записать в файл
                            with open('available_usernames.txt', 'a', encoding='utf-8') as out:
                                out.write(f"{username}\n")
                        else:
                            print(f"❌ Занят: @{username}")
                    except Exception as e:
                        print(f"⚠️ Ошибка при проверке @{username}: {e}")
                    
                    await asyncio.sleep(random.uniform(1.5, 3.0))
        
        return available

class Channel:
    def __init__(self, account: Account):
        self.account = account
    
    async def _get_client(self) -> TelegramClient:
        session_path = os.path.join(SESSIONS_DIR, f"{self.account.phone}_session")
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        client = TelegramClient(session_path, self.account.api_id, self.account.api_hash)
        await client.connect()
        return client
    
    async def join_to_channel(self, channel_username):
        try:
            async with await self._get_client() as client:
                await client(functions.channels.JoinChannelRequest(channel_username))
                print(f"Успешно вступили в канал {channel_username}")
        except Exception as e:
            print(f"Ошибка при вступлении в канал: {e}")

    async def like_post(self):
        pass

    async def comment_post(self):
        pass

    async def resend_post(self):
        pass
    
    async def mute_channel(self):
        pass