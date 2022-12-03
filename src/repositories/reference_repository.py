from database_connection import get_database_connection
from entities.reference import Reference


class ReferenceRepository:

    def __init__(self, connection=get_database_connection()):
        self._connection = connection

    def get_all(self):
        all_data = []

        cursor = self._connection.cursor()

        cursor.execute('''SELECT
                citekey,
                author,
                title,
                publisher,
                journal,
                year,
                volume_or_number,
                volume,
                number,
                pages,
                series,
                address,
                edition,
                month,
                note FROM REFERENCE''')

        rows = cursor.fetchall()
        for row in rows:
            all_data.append(dict(zip(row.keys(), row)))

        return all_data

    def add_reference(self, reference_object: Reference):
        cursor = self._connection.cursor()

        reference = reference_object.get_fields()

        cursor.execute('''
            INSERT INTO REFERENCE
                (citekey,
                author,
                title,
                publisher,
                journal,
                year,
                volume_or_number,
                volume,
                number,
                pages,
                series,
                address,
                edition,
                month,
                note)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       [reference.get("citekey"),
                        reference.get("author"),
                        reference.get("title"),
                        reference.get("publisher"),
                        reference.get("journal"),
                        reference.get("year"),
                        reference.get("volume"),
                        reference.get("volume_or_number"),
                        reference.get("number"),
                        reference.get("pages"),
                        reference.get("series"),
                        reference.get("edition"),
                        reference.get("address"),
                        reference.get("month"),
                        reference.get("note")
                        ]
                       )

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM REFERENCE')

    def citekey_is_available(self, citekey: str):
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT *
            FROM REFERENCE
            WHERE citekey=?
        ''', [citekey])

        result = cursor.fetchone()

        return bool(not result)

    def fetch_selected_references_data_fields(self, citekey: str) -> dict:
        """Returns a dictionary containing the data fields of the selected reference. If citekey is invalid, an empty dictionary is returned.

        Args:
            citekey (str): citekey of the reference

        Returns:
            dict: contains the datafields of the requested reference. If no reference is found, an empty dictionary is returned.
        """
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT *
            FROM REFERENCE
            WHERE citekey=?
        ''', [citekey])

        row = cursor.fetchone()
        if not row:
            return {}
        result = dict(zip(row.keys(), row))
        return result

    def delete_selected_reference(self, citekey: str) -> str:
        cursor = self._connection.cursor()
        if not self.citekey_is_available(citekey):

            cursor.execute('''
                DELETE FROM REFERENCE
                WHERE citekey=?
            ''', [citekey])

            self._connection.commit()

            return citekey

        return ""

    def edit_selected_reference(self, reference: Reference):
        citekey = reference.get_fields()["citekey"] or ""
        if self.citekey_is_available(citekey):
            return
        self.delete_selected_reference(citekey)
        self.add_reference(reference)


default_reference_repository = ReferenceRepository(get_database_connection())
