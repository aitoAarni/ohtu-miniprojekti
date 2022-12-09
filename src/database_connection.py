import sqlite3
from config import DATABASE_FILE_PATH
from config import TEST_DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
test_connection = sqlite3.connect(TEST_DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row
test_connection.row_factory = sqlite3.Row


def get_database_connection():
    """A method for returning the connection object
    Returns:
        connection (connect object): an object that enables the database connection.
    """
    return connection


def get_test_database_connection():
    """A method for returning the connection object
    Returns:
        connection (connect object): an object that enables the database connection.
    """
    return test_connection
