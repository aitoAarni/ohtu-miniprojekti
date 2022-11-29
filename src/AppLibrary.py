from stub_io import StubIO
from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository



class AppLibrary:
    def __init__(self) -> None:
        self._reference_service = ReferenceService(default_reference_repository)
        self._stub_io = StubIO()
        self._interface = Interface(self._reference_service, self._stub_io)

    def delete_records_from_database(self):
        self._reference_service.reference_repository.delete_all()

    def add_input(self, value):
        self._stub_io.add_input(value)

    def add_reference_input(self, value):
        self._stub_io.add_reference_field(value)


    def run_application(self):
        self._stub_io.inputs = self._stub_io.inputs + [""] * (15 -len(self._stub_io.inputs)) + ["list"] + ["exit"]
        self._interface.start()


    def clear_inputs(self):
        self._stub_io.clear_inputs()
        

    def output_should_contain(self):
        references = self._interface.reference_service.get_all_references()[0]
        for test_input in self._stub_io.added:
            if test_input not in references.values():
                raise AssertionError(f"test input {test_input}  is not in references {references}")