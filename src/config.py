import os

# Абсолютный путь к корню проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к папке сессий (src/utils/tg_tools/sessions)
SESSIONS_DIR = os.path.join(BASE_DIR, 'utils', 'tg_tools', 'sessions')
os.makedirs(SESSIONS_DIR, exist_ok=True)
