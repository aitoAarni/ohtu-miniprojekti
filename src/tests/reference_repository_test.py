import unittest
from initialize_database import initialize_database
from repositories.reference_repository import default_reference_repository
from repositories.reference_repository import ReferenceRepository
from entities.reference import Reference


class TestReferenceRepository(unittest.TestCase):

    def setUp(self):
        self.db = initialize_database()
        self.reference_repository = default_reference_repository

    def test_get_all_returns_three_entries(self):
        result = self.reference_repository.get_all()
        self.assertEqual(3, len(result))

    def test_add_article_succeeds(self):
        reference = Reference()
        reference.fields = {
            "author": "Cat McMuffin",
            "title": "Meow",
            "journal": "Catnip daily",
            "year": 2020,
            "volume": "22",
            "pages": 1
        }
        self.reference_repository.add_reference(reference)
        result = self.reference_repository.get_all()
        self.assertEqual(4, len(result))
