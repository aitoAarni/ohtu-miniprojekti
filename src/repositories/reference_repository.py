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
                volume_or_number,
                series,
                address,
                edition,
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
                str(row["volume_or_number"]),
                str(row["series"]),
                str(row["address"]),
                str(row["edition"]),
                str(row["month"]),
                str(row["note"]),
            ))
        return all_data

    def add_reference(self, reference_object: Reference):
        cursor = self._connection.cursor()

        reference = reference_object.data()

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


default_reference_repository = ReferenceRepository(get_database_connection())
