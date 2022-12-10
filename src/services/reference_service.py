import os
from entities.reference import Reference
from config import EXPORT_PATH, IMPORT_PATH
from .bib_export import BibExport
from .bib_import import BibImport

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
        self.reference = None
        self.export_directory = EXPORT_PATH
        self.import_directory = IMPORT_PATH

    def get_template_reference(self):
        self.reference = Reference()
        return self.reference.get_fields()

    def get_required_fields(self):
        return self.reference.get_required_fields()

    def save_reference(self, fields_dict :dict):
        for key, value in fields_dict.items():
            self.reference.set_field(key, value)
        self.reference_repository.add_reference(self.reference)

    def get_all_references(self):
        references = self.reference_repository.get_all()
        return references

    def check_data_validity(self, field, user_input):
        if not user_input:
            return 'Input required'

        if field == 'citekey':
            all_references = self.get_all_references()
            for reference in all_references:
                if user_input == reference['citekey']:
                    return 'Citekey taken'

        if field == 'author':
            if any(char.isdigit() for char in user_input):
                return 'Digits not allowed'

        if field == 'year':
            #for char in user_input:
                if not user_input.isdigit():
                    return 'Only digits allowed'

        return True

    def check_bib_name_validity(self, name):
        if not name:
            return 'Input required'

        for char in name:
            if char == ' ':
                return 'Spaces not allowed, use "_"'

        path = f'{self.export_directory}/{name}.bib'
        if os.path.exists(path):
            return 'Name taken'

        return True

    def create_bib(self, name):
        bib = BibExport(f'{name}.bib')
        references = self.get_all_references()
        bib.create_bib_export(references)

    def delete_reference_by_citekey(self, citekey):
        result = self.reference_repository.delete_selected_reference(citekey)
        return result

    def edit_reference(self, reference):
        new_reference = Reference()
        for key, value in reference.items():
            new_reference.set_field(key, value)
        return self.reference_repository.update_selected_reference(new_reference)

    def get_reference(self, citekey):
        reference = self.reference_repository.fetch_selected_references_data_fields(citekey)
        return reference

    def get_importable_files(self):
        path = self.import_directory
        all_files = os.listdir(path)
        bib_files = []
        for file in all_files:
            if file[-4:] == '.bib':
                bib_files.append(file)
        return bib_files

    def import_file(self, file_name:str) -> list:
        bib = BibImport()
        reference_entities_list = bib.create_reference_entities(file_name)
        #print(reference_entities_list) #this is for testing
        imported_references = self.reference_repository.add_references_from_bib_file(reference_entities_list)
        imported_citekeys = [reference.get_fields()['citekey'] for reference in imported_references]
        return imported_citekeys
