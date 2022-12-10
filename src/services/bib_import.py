from entities.reference import Reference
from .file_management import default_file_management

class BibImport:

    def __init__(self):
        """Imports bib-files created with this application.
        """
        self.filemanager = default_file_management

    def create_reference_entities(self, filename: str):
        content = self.filemanager.read_document(filename)

        list_of_references = []
        reference = ""
        for row in content.splitlines():
            if len(row) > 1:
                reference += ";" + row
            elif len(reference) > 1:
                list_of_references.append(reference)
                reference = ""

        references = []
        for item in list_of_references:
            ref = item.split(";")
            reference = Reference()
            for row in ref:
                if not row:
                    continue
                if row[0] == "@":
                    parts = row.split("{")
                    reference.set_field("citekey", parts[1])
                elif len(row) > 1:
                    parts = row.split("=")
                    reference.set_field(parts[0][4:-1], parts[1][2:-2])
            references.append(reference)
        return references
