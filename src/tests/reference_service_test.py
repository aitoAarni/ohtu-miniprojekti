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
            'citekey': None,
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
        self.reference_service.save_reference({'title': 'test'})

        self.assertEqual(self.reference_service.reference.fields['title'], reference_correct_fields['title'])


    def test_get_all_references(self):
        references = self.reference_service.get_all_references()

        self.assertEqual(len(references), 3)


