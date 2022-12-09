from repositories.reference_repository import ReferenceRepository
from database_connection import get_database_connection

class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def input_reference(self, x):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def output_reference(self, output):
        self.outputs.append(output)

    def add_input(self, value):
        self.inputs.append(value)
