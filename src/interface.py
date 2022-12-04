
class Interface:
    def __init__(self, reference_service, user_input):
        self.reference_service = reference_service
        self.user_io = user_input

    def start(self):
        while True:
            command = self.user_io.input_reference(
                "Enter command: (new, list, export, exit): ").lower()

            if command == "exit":
                self.user_io.output_reference("Exit selected, goodbye")
                return "Exit selected, goodbye"

            print("")
            self.command_selector(command)

    def command_selector(self, command):
        if command == "new":
            fields_dict = self.new_reference()
            self.reference_service.save_reference(fields_dict)
        elif command == "list":
            self.list_references()
        elif command == "export":
            file_name = self.create_name_for_bib()
            self.create_bib(file_name)

    def new_reference(self):
        fields_dict = self.reference_service.get_template_reference()
        required_fields_list = self.reference_service.get_required_fields()

        for field in required_fields_list:
            user_input = self.user_io.input_reference(f"\t Enter {field}: ")
            validity = self.reference_service.check_data_validity(field, user_input)
            while validity is not True:
                self.user_io.output_reference(validity)
                user_input = self.user_io.input_reference(f"\t Enter {field}: ")
                validity = self.reference_service.check_data_validity(field, user_input)
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
                self.user_io.output_reference(f"  └── {key}: {value}")
            else:
                self.user_io.output_reference(f"  ├── {key}: {value}")
        self.user_io.output_reference("\n")

    def create_name_for_bib(self):
        user_input = self.user_io.input_reference("\t Enter a name for your bib file: ")
        validity = self.reference_service.check_bib_name_validity(user_input)
        while validity is not True:
            self.user_io.output_reference(validity)
            user_input = self.user_io.input_reference("\t Enter a name for your bib file: ")
            validity = self.reference_service.check_bib_name_validity(user_input)
        return user_input

    def create_bib(self, file_name):
        self.reference_service.create_bib(file_name)
        self.user_io.output_reference("Bib file saved into saved_exports directory\n")
