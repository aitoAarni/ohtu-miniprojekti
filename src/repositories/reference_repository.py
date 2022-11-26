from database_connection import get_database_connection
from entities.reference import Reference


class ReferenceRepository:

    def __init__(self, connection=get_database_connection()):
        self._connection = connection
        pass

    def get_all(self):
        all_data = []
        cursor = self._connection.cursor()

        cursor.execute('''SELECT 
                citekey,
                author,
                title,
                journal,
                year,
                volume,
                number, 
                pages,
                month,
                note FROM REFERENCE''')

        rows = cursor.fetchall()
        for row in rows:
            all_data.append((
                str(row["citekey"]),
                str(row["author"]),
                str(row["title"]),
                str(row["journal"]),
                str(row["year"]),
                str(row["volume"]),
                str(row["number"]),
                str(row["pages"]),
                str(row["month"]),
                str(row["note"]),
            ))
        return all_data

    def add_article_reference(self, reference_object: Reference):
        cursor = self._connection.cursor()

        reference = reference_object.data()

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
                VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                       [reference["citekey"],
                        reference["author"],
                        reference["title"],
                        reference["journal"],
                        reference["year"],
                        reference["volume"],
                        reference["number"],
                        reference["pages"],
                        reference["month"],
                        reference["note"]]
                       )


default_reference_repository = ReferenceRepository(get_database_connection())
