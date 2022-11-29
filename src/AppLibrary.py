from stub_io import StubIO
from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository

class AppLibrary:
    def __init__(self) -> None:
        self._reference_service = ReferenceService(default_reference_repository)
        self._stub_io = StubIO()
        self._interface = Interface(self._reference_service, self._stub_io)
        self.test_inputs = []

    def input(self, value):
        self._stub_io.add_input(value)

    def run_application(self):
        self._interface.start()

    def clear_inputs(self):
        self._stub_io.clear_inputs()

    def initialize_test(self):
        print("testi 123")
        self.test_inputs.clear()
        print("database referenssit", self._reference_service.get_all_references())

    def database_should_contain_right_reference(self):
        pass

    def print_message(self, msg):
        print(msg)
