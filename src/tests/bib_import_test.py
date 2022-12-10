import os
import unittest
from services.bib_import import BibImport
from services.file_management import default_file_management as filemanager


class TestBibExport(unittest.TestCase):

    def test_create_reference_entities_reads_file(self):
        filepath = os.path.join(filemanager.import_directory, 'test.bib')
        with open(filepath, 'w', encoding="utf-8") as file:
            file.write('''
@article{testcormen01,
    author = {Cormen et. al.},
    title = {Data Structures and Algorithms},
    journal = {Fantastic Algorithms},
    year = {2000},
    volume = {vol. 202},
    pages = {14},
    month = {11},
    note = {my favorite article},
}
            ''')
        bib_importer = BibImport()
        references = bib_importer.create_reference_entities('test.bib')
        os.remove(filepath)

        self.assertEqual(len(references), 1)
