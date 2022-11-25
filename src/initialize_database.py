from database_connection import get_database_connection


def drop_tables(connection):
    """Destroys the tables from the database.
    Args:
        connection (connect object): an object that enables the database connection.
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS REFERENCE;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS TAGS;
    ''')

    connection.commit()


def create_tables(connection):
    """Creates database tables for the application
    Args:
        connection (connect object): an object that enables the database connection.
    """
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE REFERENCE (
            citekey TEXT UNIQUE NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT NOT NULL,
            year INTEGER NOT NULL,
            volume_or_number TEXT,
            series TEXT,
            address TEXT,
            edition TEXT,
            month INTEGER,
            note TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE TAGS (
            citekey TEXT,
            tag TEXT
        );
    ''')

    connection.commit()


def create_mock_data(connection):
    """Creates mock-data to test database in initial build. Remove this when the database is setup and tests are configured.

    Args:
        connection (connect object): an object that enables database connection
    """

    cursor = connection.cursor()

    references = []

    reference1 = {
        "citekey": "cormen01",
        "author": "Cormen et. al.",
        "title": "Data Structures and Algorithms",
        "journal": "Fantastic Algorithms",
        "year": 2000,
        "volume_or_number": "vol. 202",
        "series": None,
        "address": "https://cormen.com",
        "edition": None,
        "month": 11,
        "note": "my favorite article"
    }

    reference2 = {
        "citekey": "cormen02",
        "author": "Cormen et. al.",
        "title": "Data Structures and Algorithms v.2",
        "journal": "Fantastic Algorithms",
        "year": 2001,
        "volume_or_number": "vol. 203",
        "series": None,
        "address": "https://cormen.com",
        "edition": None,
        "month": 12,
        "note": "my 2nd favorite article"
    }

    reference3 = {
        "citekey": "martin01",
        "author": "Uncle Bob",
        "title": "Agile is hip",
        "journal": "Agile-fans",
        "year": 2011,
        "volume_or_number": None,
        "series": None,
        "address": "https://uncle-bob.com",
        "edition": None,
        "month": 1,
        "note": "Controversial stuff"
    }

    references.append(reference1)
    references.append(reference2)
    references.append(reference3)

    for reference in references:
        cursor.execute('''
            INSERT INTO REFERENCE
                (citekey,
                author,
                title,
                journal,
                year,
                volume_or_number,
                series,
                address,
                edition,
                month,
                note)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                       [reference["citekey"],
                        reference["author"],
                        reference["title"],
                        reference["journal"],
                        reference["year"],
                        reference["volume_or_number"],
                        reference["series"],
                        reference["address"],
                        reference["edition"],
                        reference["month"],
                        reference["note"]]
                       )


def initialize_database():
    """Calls a method to activate the object that enables database connection.
    Calls methods to delete and create tables to database.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    create_mock_data(connection)


if __name__ == "__main__":
    initialize_database()
