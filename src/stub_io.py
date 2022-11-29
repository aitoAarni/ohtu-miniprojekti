class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []


    def input_reference(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def output_reference(self, output):
        self.outputs.append(output)


    def add_input(self, value):
        self.inputs.append(value)
    
    def clear_inputs(self):
        self.inputs.clear()