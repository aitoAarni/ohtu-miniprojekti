import unittest
from initialize_database import initialize_database
from repositories.reference_repository import default_reference_repository
from repositories.reference_repository import ReferenceRepository


class TestReferenceRepository(unittest.TestCase):

    def setup(self):
        self.db = initialize_database()
        self.reference_repository = default_reference_repository

    def test_get_all_returns_three_entries(self):
        self.reference_repository = ReferenceRepository()
        result = self.reference_repository.get_all()
        self.assertEqual(3, len(result))
