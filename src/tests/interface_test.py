import unittest
from ui.interface import Interface
from ui.commands import list_references
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository
from stub_io import StubIO
from initialize_database import initialize_database


class TestInterface(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.reference_repository = default_reference_repository
        self.reference_service = ReferenceService(self.reference_repository)
        self.user_io = StubIO()
        self.interface = Interface(self.reference_service, self.user_io)

    def test_exit_command_stops_program(self):
        self.user_io.add_input("exit")

        result = self.interface.start()
        self.user_io.input_reference("")

        self.assertEqual(result, "Exit selected, goodbye")

    def test_new_command_adds_a_new_reference_with_proper_input(self):
        start_db = self.reference_repository.get_all()

        self.user_io.add_input("new")
        self.user_io.add_input("citekey")
        self.user_io.add_input("author")
        self.user_io.add_input("title")
        self.user_io.add_input("journal")
        self.user_io.add_input("1997")
        self.user_io.add_input("tag")
        self.user_io.add_input("exit")

        self.interface.start()

        while True:
            output = self.user_io.input_reference("")
            if not output:
                break

            return output

        end_db = self.reference_repository.get_all()

        self.assertEqual(len(end_db), len(start_db)+1)

    def test_list_references_returns_all_references(self):
        db = self.reference_repository.get_all()
        result = list_references(self.reference_service, self.user_io)

        self.assertEqual(db, result)

    def test_delete_reference_with_valid_citekey(self):
        result = self.reference_service.delete_reference_by_citekey("martin01")
        self.assertEqual(result, "martin01")

    def test_delete_reference_with_not_valid_citekey(self):
        result = self.reference_service.delete_reference_by_citekey("iida")
        self.assertEqual(result, "")
