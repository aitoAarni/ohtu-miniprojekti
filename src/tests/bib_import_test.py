import os
import unittest
from services.bib_import import BibImport
from AppLibrary import AppLibrary

class TestBibExport(unittest.TestCase):

    def test_create_reference_entities_reads_file(self):
        filepath = AppLibrary().create_bib_file_for_robot_test('test.bib')
        bib_importer = BibImport()
        references = bib_importer.create_reference_entities('test.bib')
        os.remove(filepath)

        self.assertEqual(len(references), 1)
