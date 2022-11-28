from entities.reference import Reference

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
    
    def get_template_reference(self):
        self.reference = Reference()
        return self.reference.fields

    def save_reference(self, fields_dict :dict):
        for key, value in fields_dict.items():
            self.reference.fields[key] = value
        self.reference_repository.add_reference(self.reference)

    def get_all_references(self):
        references = self.reference_repository.get_all()
        return references
