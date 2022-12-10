import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

export_dir = os.getenv("DEFAULT_EXPORT_PATH") or "saved_exports"
import_dir = os.getenv("DEFAULT_IMPORT_PATH") or "imports"

EXPORT_PATH = os.path.join(dirname, '..', export_dir)
IMPORT_PATH = os.path.join(dirname, '..', import_dir)

if not os.path.exists(EXPORT_PATH):
    os.makedirs(EXPORT_PATH)

if not os.path.exists(IMPORT_PATH):
    os.makedirs(IMPORT_PATH)


DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
TEST_DATABASE_FILENAME = os.getenv(
    'TEST_DATABASE_FILENAME') or 'test-database.db'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
TEST_DATABASE_FILE_PATH = os.path.join(
    dirname, '..', 'data', TEST_DATABASE_FILENAME)
