from stub_io import StubIO
from ui.interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_test_reference_repository


class AppLibrary:
    def __init__(self) -> None:
        self._reference_service = ReferenceService(
            default_test_reference_repository)
        self._stub_io = StubIO()
        self._interface = Interface(self._reference_service, self._stub_io)

    def delete_all_records_from_database(self):
        self._reference_service.reference_repository.delete_all()

    def add_input(self, value):
        self._stub_io.add_input(value)

    def run_application(self):
        self._interface.start()
    #pylint: disable=too-many-arguments

    def create_reference_to_database(self, citekey, author, title, journal, year):
        reference_dict = {
            "citekey": citekey,
            "author": author,
            "title": title,
            "journal": journal,
            "year": int(year)
        }
        # get_template_reference() is called to change ReferenceService
        # object's reference attribute
        # to have a reference object in it (initially it is None)
        self._reference_service.get_template_reference()
        self._reference_service.save_reference(reference_dict)

    def output_should_contain(self, *fields):
        keys = self._reference_service.get_required_fields()
        user_passed_fields_dict = {
            keys[i]: field for i, field in enumerate(fields)}
        references = self.get_all_references()
        for test_input in references:
            user_record_in_database = True
            for key, user_input in user_passed_fields_dict.items():
                if str(test_input[key]) != user_input:
                    user_record_in_database = False
            if user_record_in_database:
                return True
        raise AssertionError(f"Fields {fields} are not in a reference")

    def get_all_references(self):
        return self._interface.reference_service.get_all_references()

    def output_should_be_empty(self):
        references = self.get_all_references()
        if len(references) != 0:
            raise AssertionError(
                "There shouldn't be any references in the database, but there are")


if __name__ == "__main__":
    app = AppLibrary()
