import os
import unittest
from entities.reference import Reference
from services.bib_export import BibExport
from services.file_management import default_file_management as filemanager


class TestBibExport(unittest.TestCase):

    def test_constructor_gets_default_filename(self):
        bib_exporter = BibExport()
        filename = bib_exporter.filename
        self.assertNotEqual(None, filename)

    def test_constructor_gets_given_filename(self):
        filename = "exported_references"
        bib_exporter = BibExport(filename)
        self.assertEqual(filename, bib_exporter.filename)

    def test_constructor_gets_export_path(self):
        bib_exporter = BibExport()
        path = filemanager.directory
        self.assertNotEqual(None, path)

    def test_create_export_writes_file(self):
        bib_exporter = BibExport("filename.bib")
        ref = Reference()
        ref.set_field("citekey", "quack")
        ref.set_field("author", "D. Duck")
        ref.set_field("title", "On hard luck")
        fields = [ref.get_fields()]
        bib_exporter.create_bib_export(fields)
        filepath = os.path.join(filemanager.directory, bib_exporter.filename)
        file_created = os.path.exists(filepath)
        self.assertEqual(file_created, True)
        if file_created:
            os.remove(filepath)
