
class Interface:
    def __init__(self, reference_service, user_input):
        self.reference_service = reference_service
        self.user_io = user_input

    def start(self):
        while True:
            command = self.user_io.input_reference(
                "Enter command: (new, list, exit): ").lower()

            if command == "exit":
                self.user_io.output_reference("Exit selected, goodbye")
                return "Exit selected, goodbye"

            print("")
            self.command_selector(command)

    def command_selector(self, command):
        if command == "new":
            fields_dict = self.new_reference()
            if not self.reference_service.save_reference(fields_dict):
                self.user_io.output_reference(
                    "There was an error in data fields and reference was not saved. (Did you add a unique citekey?)")
        elif command == "list":
            self.list_references()

    def new_reference(self):
        fields_dict = self.reference_service.get_template_reference()

        for field in fields_dict:
            user_input = self.user_io.input_reference(f"\t Enter {field}: ")
            fields_dict[field] = user_input

        return fields_dict

    def list_references(self):
        references = self.reference_service.get_all_references()

        for reference in references:
            self.print_reference_objects(reference)

        return references

    def print_reference_objects(self, reference):
        last_key = list(reference.keys())[-1]

        for key, value in reference.items():
            if not value:
                continue

            if key == "citekey":
                self.user_io.output_reference(f"{key} {value}")
            elif key == last_key:
                self.user_io.output_reference(f"  └── {key}: {value} \n")
            else:
                self.user_io.output_reference(f"  ├── {key}: {value}")
