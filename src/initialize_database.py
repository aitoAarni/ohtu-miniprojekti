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
            citekey TEXT UNIQUE,
            author TEXT,
            title TEXT,
            publisher TEXT,
            journal TEXT,
            year INTEGER,
            volume_or_number TEXT,
            volume TEXT,
            number INTEGER,
            pages INTEGER,
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
        "volume": "vol. 202",
        "number": None,
        "pages": 14,
        "month": 11,
        "note": "my favorite article"
    }

    reference2 = {
        "citekey": "cormen02",
        "author": "Cormen et. al.",
        "title": "Data Structures and Algorithms v2.",
        "journal": "Fantastic Algorithms vol II",
        "year": 2014,
        "volume": "vol. 232",
        "number": None,
        "pages": 214,
        "month": 2,
        "note": "my 2nd favorite article"
    }

    reference3 = {
        "citekey": "martin01",
        "author": "Uncle Bob",
        "title": "Agile is hip",
        "journal": "Agile-fans",
        "year": 2011,
        "volume": None,
        "number": None,
        "pages": 11,
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
                volume,
                number,
                pages,
                month,
                note)
                VALUES (?,?,?,?,?,?,?,?,?,?)''',
                       [reference.get("citekey"),
                        reference.get("author"),
                        reference.get("title"),
                        reference.get("journal"),
                        reference.get("year"),
                        reference.get("volume"),
                        reference.get("number"),
                        reference.get("pages"),
                        reference.get("month"),
                        reference.get("note")]
                       )

        connection.commit()


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
