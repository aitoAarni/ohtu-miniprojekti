class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []


    def output_reference(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value):
        self.inputs.append(value)
    
    def clear_inputs(self):
        self.inputs.clear()