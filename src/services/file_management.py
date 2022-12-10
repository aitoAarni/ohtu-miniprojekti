import os
from config import EXPORT_PATH, IMPORT_PATH


class FileManagement:

    def __init__(self):
        """A constructor for the class.

        Args:
            filename (str, optional): A user given filename. Please note that filename should contain .bib extension.
            This is not validated in this class. Defaults to 'export.bib'.
        """
        self.export_directory = EXPORT_PATH
        self.import_directory = IMPORT_PATH

    def write_document(self, content: str, filename: str):
        """Writes content to given filename. Please note that mode is set to write, which overwrites file, if file already exists.

        Args:
            content (str): bibtext-references as a string.
        """
        file_and_directory = os.path.join(self.export_directory, filename)
        with open(file_and_directory, "w", encoding="utf-8") as file:
            file.write(content)

    def read_document(self, filename: str) -> str:
        with open(f'{self.import_directory}/{filename}', 'r', encoding="utf-8") as f:
            output = f.read()
        return output


default_file_management = FileManagement()
