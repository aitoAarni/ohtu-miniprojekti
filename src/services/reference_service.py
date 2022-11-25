from entities.reference import Reference

class ReferenceService:
    def __init__(self, reference_repository):
        self.reference_repository = reference_repository
    
    def get_template_reference(self):
        return Reference()

    def save_reference(self, reference :Reference):
        self.reference_repository.add_reference(reference)
