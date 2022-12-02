from config import EXPORT_PATH
import os
from entities.reference import Reference


class BibExport:

    def __init__(self, filename='export.bib'):
        """A constructor for the class. 

        Args:
            filename (str, optional): A user given filename. Please note that filename should contain .bib extension. This is not validated in this class. Defaults to 'export.bib'.
        """
        self.directory = EXPORT_PATH
        self.filename = filename

    def write_document(self, content: str):
        """Writes content to given filename. Please note that mode is set to write, which overwrites file, if file already exists. 

        Args:
            content (str): bibtext-references as a string. 
        """
        file_and_directory = os.path.join(self.directory, self.filename)
        with open(file_and_directory, "w", encoding="utf-8") as file:
            file.write(content)

    def create_bib_export(self, references: list):
        """Creates a bibtex-string containing content from all non-empty data fields in given Reference-objects

        Args:
            references (list): Receives a list of Reference objects from the service class.
        """
        output = ""
        for reference in references:
            bib_reference = "@article{" + reference.fields["citekey"] + ",\n"
            for key, item in reference.fields.items():
                if key == "citekey":
                    continue
                if item:
                    bib_reference += "    " + key + " = {" + str(item) + "},\n"
            bib_reference += "}\n\n"
            output += bib_reference

        self.write_document(output)
