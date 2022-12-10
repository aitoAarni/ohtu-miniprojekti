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
            note TEXT,
            tag TEXT
        );
    ''')

    connection.commit()


def create_mock_data(connection):
    """Creates mock-data to test database in initial build. This was a requirement for the client's demo session.

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
        "note": "my favorite article",
        "tag": None
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
        "note": "my 2nd favorite article",
        "tag": "thesis"
    }

    reference3 = {
        "citekey": "martin01",
        "author": "Uncle Bob",
        "title": "The Agile hip-revolution",
        "journal": "Agile-fans",
        "year": 2011,
        "volume": None,
        "number": None,
        "pages": 11,
        "month": 1,
        "note": "Controversial stuff",
        "tag": "fun"
    }

    reference4 = {
        "citekey": "sipser01",
        "author": "M. Sipser",
        "title": "Computate this!",
        "journal": "Hardcore CS-fans daily",
        "year": 2018,
        "volume": None,
        "number": None,
        "pages": 262,
        "month": 2,
        "note": "Fantastic but a bit brief article",
        "tag": "thesis"
    }

    reference5 = {
        "citekey": "gur07",
        "author": "Gabriel Uru",
        "title": "GNU or out!",
        "journal": "GNUru journal",
        "year": 2014,
        "volume": None,
        "number": None,
        "pages": 262,
        "month": 2,
        "note": "Unreadable",
        "tag": "shellscripting"
    }

    references.append(reference1)
    references.append(reference2)
    references.append(reference3)
    references.append(reference4)
    references.append(reference5)

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
                note,
                tag)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                       [reference.get("citekey"),
                        reference.get("author"),
                        reference.get("title"),
                        reference.get("journal"),
                        reference.get("year"),
                        reference.get("volume"),
                        reference.get("number"),
                        reference.get("pages"),
                        reference.get("month"),
                        reference.get("note"),
                        reference.get("tag")]
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
