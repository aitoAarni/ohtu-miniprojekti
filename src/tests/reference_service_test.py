import unittest
from unittest.mock import Mock
from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.reference_repository_mock = Mock(wraps=ReferenceRepository())
        self.reference_service = ReferenceService(self.reference_repository_mock)

    def test_save_reference_creates_correct_dict(self):
        reference_correct_fields = {
            'address': None,
            'author': None,
            'citekey': 'citekey1',
            'edition': None,
            'journal': None,
            'month': None,
            'note': None,
            'number': None,
            'pages': None,
            'publisher': None,
            'series': None,
            'title': 'test',
            'volume': None,
            'volume_or_number': None,
            'year': None
        }

        self.reference_service.get_template_reference()
        self.reference_service.save_reference({'title': 'test', 'citekey': 'citekey1'})

        self.assertEqual(self.reference_service.reference.get_fields()['title'], reference_correct_fields['title'])

    def test_check_data_validity_returns_correct_str_when_no_citekey(self):
        result = self.reference_service.check_data_validity('citekey', None)

        self.assertEqual(result, 'Input required')

    def test_check_data_validity_returns_correct_str_when_citekey_taken(self):
        result = self.reference_service.check_data_validity('citekey', 'cormen01')

        self.assertEqual(result, 'Citekey taken')

    def test_check_data_validity_returns_correct_str_when_author_contains_digits(self):
        result = self.reference_service.check_data_validity('author', 'ou jea1')

        self.assertEqual(result, 'Digits not allowed')

    def test_check_data_validity_returns_correct_str_when_year_contains_letters(self):
        result = self.reference_service.check_data_validity('year', '8y')

        self.assertEqual(result, 'Only digits allowed')

    def test_check_data_validity_returns_True(self):
        result = self.reference_service.check_data_validity('citekey', 'cormen05')

        self.assertEqual(result, True)

    def test_get_all_references_right_citekeys(self):
        references = self.reference_service.get_all_references()
        references_citekeys = references[0]['citekey'], references[1]['citekey']
        citekeys = "cormen01", "cormen02"

        self.assertEqual(references_citekeys, citekeys)

    def test_check_bib_name_validity_returns_correct_str_when_no_name_given(self):
        result = self.reference_service.check_bib_name_validity(None)

        self.assertEqual(result, 'Input required')

    def test_check_bib_name_validity_returns_correct_str_when_name_contains_spaces(self):
        result = self.reference_service.check_bib_name_validity('te st')

        self.assertEqual(result, 'Spaces not allowed, use "_"')

    def test_delete_reference_by_citekey(self):
        result = self.reference_repository_mock.delete_selected_reference("martin01")
        self.assertEqual(result, "martin01")

    def test_get_reference_by_citekey(self):
        reference = self.reference_service.get_reference("cormen01")
        self.assertEqual(reference["title"], "Data Structures and Algorithms")

    def test_get_importable_files_returns_a_list(self):
        file_list = self.reference_service.get_importable_files()
        self.assertEqual(type(file_list), list)
