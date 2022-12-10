import unittest
from initialize_database import initialize_database
from repositories.reference_repository import default_reference_repository
from entities.reference import Reference


class TestReferenceRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.reference_repository = default_reference_repository

    def add_reference(self, citekey):
        reference = Reference()
        reference._fields = {
            "citekey": citekey,
            "author": "Cat McMuffin",
            "title": "Meow",
            "journal": "Catnip daily",
            "year": 2020,
            "volume": "22",
            "pages": 1
        }
        self.reference_repository.add_reference(reference)

    def test_get_all_returns_three_entries(self):
        result = self.reference_repository.get_all()
        self.assertEqual(5, len(result))

    def test_add_article_succeeds(self):
        reference = Reference()
        reference._fields = {
            "author": "Cat McMuffin",
            "title": "Meow",
            "journal": "Catnip daily",
            "year": 2020,
            "volume": "22",
            "pages": 1
        }
        self.reference_repository.add_reference(reference)
        result = self.reference_repository.get_all()
        self.assertEqual(6, len(result))

    def test_citekey_is_not_available_returns_false(self):
        result = self.reference_repository.citekey_is_available('martin01')
        self.assertEqual(result, False)

    def test_citekey_is_available_returns_true(self):
        result = self.reference_repository.citekey_is_available('martin02')
        self.assertEqual(result, True)

    def test_update_article_succeeds(self):
        reference = Reference()
        reference._fields = {
            "citekey": "Cat01",
            "author": "Cat McMuffin",
            "title": "Meow",
            "journal": "Catnip daily",
            "year": 2020,
            "volume": "22",
            "pages": 1
        }
        self.reference_repository.add_reference(reference)
        reference.set_field("author", "Dog McMuffin")
        self.reference_repository.update_selected_reference(reference)
        citekey = reference._fields["citekey"]
        updated_reference = self.reference_repository.fetch_selected_references_data_fields(
            citekey)
        self.assertEqual(
            reference._fields["author"], updated_reference["author"])

    def test_update_returns_with_no_edit_if_citekey_is_wrong(self):
        reference = Reference()
        reference._fields = {
            "citekey": "Cat01",
            "author": "Cat McMuffin",
            "title": "Meow",
            "journal": "Catnip daily",
            "year": 2020,
            "volume": "22",
            "pages": 1
        }
        self.reference_repository.add_reference(reference)
        reference.set_field("author", "Dog McMuffin")
        reference.set_field("citekey", "Cat02")
        self.reference_repository.update_selected_reference(reference)
        updated_reference = self.reference_repository.fetch_selected_references_data_fields(
            "Cat01")
        self.assertEqual(
            "Cat McMuffin", updated_reference["author"])

    def test_delete_all_works(self):
        entries = self.reference_repository.get_all()
        self.reference_repository.delete_all()
        entries_after_deletion = self.reference_repository.get_all()
        self.assertEqual(len(entries_after_deletion) +
                         len(entries), len(entries))

    def test_delete_selected_works(self):
        citekey = "Cato01"
        self.add_reference(citekey)
        self.reference_repository.delete_selected_reference(citekey)
        fetched_reference = self.reference_repository.fetch_selected_references_data_fields(
            citekey)
        self.assertEqual(len(fetched_reference), 0)

    def test_nothing_is_deleted_with_wrong_citekey(self):
        entries = self.reference_repository.get_all()
        self.reference_repository.delete_selected_reference("unused_citekey")
        entries_after_deletion = self.reference_repository.get_all()
        self.assertEqual(len(entries), len(entries_after_deletion))

    def test_fetch_matching_reference_fetches_right_reference(self):
        citekey1 = "Cato01"
        citekey2 = "Doggo01"
        self.reference_repository.delete_all()
        self.add_reference(citekey1)
        self.add_reference(citekey2)
        reference_list = self.reference_repository.fetch_matching_references(
            "ato")
        self.assertEqual(len(reference_list), 1)

    def test_fetch_matching_reference_fetches_all_matching_references(self):
        citekey1 = "Cato01"
        citekey2 = "Doggo01"
        citekey3 = "Puppie01"
        self.reference_repository.delete_all()
        self.add_reference(citekey1)
        self.add_reference(citekey2)
        self.add_reference(citekey3)
        reference_list = self.reference_repository.fetch_matching_references(
            "o01")
        self.assertEqual(len(reference_list), 2)
