import unittest
from unittest.mock import Mock, ANY
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

        self.assertEqual(self.reference_service.reference.fields['title'], reference_correct_fields['title'])

    def test_save_reference_returns_false_when_citekey_taken(self):
        self.reference_service.get_template_reference()
        result = self.reference_service.save_reference({'citekey': 'cormen01'})

        self.assertEqual(result, False)

    def test_check_data_validity_returns_false_when_no_citekey(self):
        result = self.reference_service.check_data_validity({'citekey': None, 'author': 'me'})

        self.assertEqual(result, False)

    def test_check_data_validity_returns_false_when_citekey_taken(self):
        result = self.reference_service.check_data_validity({'citekey': 'cormen01', 'author': 'me'})

        self.assertEqual(result, False)

    def test_get_all_references_right_citekeys(self):
        references = self.reference_service.get_all_references()
        references_citekeys = references[0]['citekey'], references[1]['citekey'], references[2]['citekey']
        citekeys = "cormen01", "cormen02", "martin01"

        self.assertEqual(references_citekeys, citekeys)


