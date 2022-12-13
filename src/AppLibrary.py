import os
from stub_io import StubIO
from ui.interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_test_reference_repository
from services.file_management import default_file_management as filemanager


class AppLibrary:
    def __init__(self) -> None:
        self._reference_service = ReferenceService(
            default_test_reference_repository)
        self._stub_io = StubIO()
        self._interface = Interface(self._reference_service, self._stub_io)

    def delete_all_records_from_database(self):
        self._reference_service.reference_repository.delete_all()

    def delete_exported_and_imported_files(self):
        export_filepath = os.path.join(
            filemanager.import_directory, 'robot-test.bib')
        import_filepath = os.path.join(
            filemanager.export_directory, 'robot-test.bib')
        if os.path.exists(export_filepath):
            os.remove(export_filepath)
        if os.path.exists(import_filepath):
            os.remove(import_filepath)

    def add_input(self, value):
        self._stub_io.add_input(value)

    def run_application(self):
        self._interface.start()
    #pylint: disable=too-many-arguments

    def create_reference_to_database(self, citekey, author, title, journal, year, tag=None):
        reference_dict = {
            "citekey": citekey,
            "author": author,
            "title": title,
            "journal": journal,
            "year": int(year),
            "tag": tag
        }
        # get_template_reference() is called to change ReferenceService
        # object's reference attribute
        # to have a reference object in it (initially it is None)
        self._reference_service.get_template_reference()
        self._reference_service.save_reference(reference_dict)

    def value_should_be_found_in_database(self, *fields):
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

    def output_contains(self, string: str):
        for item in self._stub_io.outputs:
            if string in item:
                return True
        raise AssertionError("No match found.")

    def get_all_references(self):
        return self._interface.reference_service.get_all_references()

    def output_should_be_empty(self):
        references = self.get_all_references()
        if len(references) != 0:
            raise AssertionError(
                "There shouldn't be any references in the database, but there are")

    def create_bib_file_for_robot_test(self):
        bib_test_file = os.path.join(
            filemanager.import_directory, 'robot-test.bib')
        with open(bib_test_file, 'w', encoding="utf-8") as file:
            file.write('''
@article{testcormen01,
    author = {Cormen et. al.},
    title = {Data Structures and Algorithms},
    journal = {Fantastic Algorithms},
    year = {2000},
    volume = {vol. 202},
    pages = {14},
    month = {11},
    note = {my favorite article},
}
            ''')


if __name__ == "__main__":
    app = AppLibrary()
