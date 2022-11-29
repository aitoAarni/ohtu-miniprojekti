from entities.reference import Reference

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
        self.reference = None

    def get_template_reference(self):
        self.reference = Reference()
        return self.reference.fields

    def save_reference(self, fields_dict :dict):
        if self.check_data_validity(fields_dict):
            for key, value in fields_dict.items():
                self.reference.fields[key] = value
            self.reference_repository.add_reference(self.reference)
            return True
        return False

    def get_all_references(self):
        references = self.reference_repository.get_all()
        return references

    def check_data_validity(self, fields_dict :dict):
        all_references = self.get_all_references()

        if not fields_dict['citekey']:
            return False

        for reference in all_references:
            if fields_dict['citekey'] == reference['citekey']:
                return False

        return True
