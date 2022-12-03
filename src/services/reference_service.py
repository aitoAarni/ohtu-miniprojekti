from entities.reference import Reference

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
        self.reference = None

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
            for char in user_input:
                if not char.isdigit():
                    return 'Only digits allowed'

        return True
