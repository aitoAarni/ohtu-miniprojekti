import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

path = os.getenv("DEFAULT_EXPORT_PATH") or "saved_exports"

EXPORT_PATH = os.path.join(dirname, '..', path)

if not os.path.exists(EXPORT_PATH):
    os.makedirs(EXPORT_PATH)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
