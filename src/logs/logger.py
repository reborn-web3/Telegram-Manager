from loguru import logger
import sys
import os
from datetime import datetime

# Удаляем стандартный обработчик (если нужно)
logger.remove()

# Настройка формата логов
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

# Базовые настройки логгера
logger.add(
    sink=sys.stdout,  # Вывод в консоль
    level="DEBUG",    # Минимальный уровень для вывода
    format=log_format,
    colorize=True,    # Цвета в консоли
    backtrace=True,   # Показывать стек вызовов при ошибках
    diagnose=True     # Подробная диагностика
)

# Логирование в файл (с ротацией)
log_file = os.path.join("logs", f"log_{datetime.now().strftime('%Y-%m-%d')}.log")
os.makedirs("logs", exist_ok=True)  # Создаём папку logs, если её нет

logger.add(
    sink=log_file,
    level="INFO",     # В файл пишем только INFO и выше
    format=log_format,
    rotation="10 MB", # Ротация при достижении 10 МБ
    retention="7 days", # Храним логи 7 дней
    compression="zip" # Архивируем старые логи
)

# Пример использования (можно удалить)
if __name__ == "__main__":
    logger.debug("Это debug-сообщение")
    logger.info("Это info-сообщение")
    logger.warning("Это warning-сообщение")
    logger.error("Это error-сообщение")
    try:
        1 / 0
    except Exception as e:
        logger.exception("Произошла ошибка:")