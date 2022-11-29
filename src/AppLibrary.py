from stub_io import StubIO
from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository



class AppLibrary:
    def __init__(self) -> None:
        self._reference_service = ReferenceService(default_reference_repository)
        self._stub_io = StubIO()
        self._interface = Interface(self._reference_service, self._stub_io)

    def input(self, value):
        self._stub_io.add_input(value)


    def run_application(self):
        self._interface.start()

    def clear_inputs(self):
        self._stub_io.clear_inputs()

    