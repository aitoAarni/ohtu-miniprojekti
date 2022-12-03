import unittest
from unittest.mock import Mock
from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        reference_repository_mock = Mock(wraps=ReferenceRepository())
        self.reference_service = ReferenceService(reference_repository_mock)

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
        references_citekeys = references[0]['citekey'], references[1]['citekey'], references[2]['citekey']
        citekeys = "cormen01", "cormen02", "martin01"

        self.assertEqual(references_citekeys, citekeys)
