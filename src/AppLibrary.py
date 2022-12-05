from stub_io import StubIO
from ui.interface import Interface
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

    def run_application(self):
        self._interface.start()

    def add_reference_to_database(self, citekey="testCitekey"):
        reference_dict = {
            "citekey": citekey,
            "author": "testAuthor",
            "title": "testTitle",
            "journal": "testJournal",
            "year": "testYear"
        }
        # get_template_reference() is called to change ReferenceService
        # object's reference attribute
        # to have a reference object in it (initially it is None)
        self._reference_service.get_template_reference()
        self._reference_service.save_reference(reference_dict)


    def output_should_contain(self, citekey):
        references = self.get_all_references()
        for test_input in references:
            if citekey == test_input["citekey"]:
                return True
        raise AssertionError(f"citekey {citekey} is not in references")

    def get_all_references(self):
        return self._interface.reference_service.get_all_references()

    def output_should_be_empty(self):
        references = self.get_all_references()
        if len(references) != 0:
            raise AssertionError("There shouldn't be any references in the database, but there are")


if __name__ == "__main__":
    pass