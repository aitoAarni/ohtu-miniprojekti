from .file_management import default_file_management

class BibExport:

    def __init__(self, filename='export.bib'):
        """A constructor for the class.

        Args:
            filename (str, optional): A user given filename. Please note that filename should contain .bib extension.
            This is not validated in this class. Defaults to 'export.bib'.
        """
        self.filename = filename
        self.filemanager = default_file_management

    def create_bib_export(self, references: list):
        """Creates a bibtex-string containing content from all non-empty data fields in given Reference-objects

        Args:
            references (list): Receives a list of Reference objects from the service class.
        """
        output = ""
        for reference in references:
            bib_reference = "@article{" + reference["citekey"] + ",\n"
            for key, item in reference.items():
                if key == "citekey":
                    continue
                if item:
                    bib_reference += "    " + key + " = {" + str(item) + "},\n"
            bib_reference += "}\r"
            output += bib_reference

        self.filemanager.write_document(output, self.filename)
