from entities.reference import Reference
from repositories.reference_repository import default_reference_repository

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
    
    def get_template_reference(self):
        return Reference()

    def save_reference(self, reference :Reference):
        self.reference_repository.add_reference(reference)

    def list_references(self):
        references = default_reference_repository.get_all()

        for reference in references:
            for key, value in reference.items():
                print(f"{key}: {value}")
            print()