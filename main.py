import asyncio

from src.utils.create_menu import create_menu

async def main():
    await create_menu()

if __name__ == "__main__":
    asyncio.run(main())