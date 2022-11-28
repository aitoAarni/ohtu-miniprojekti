
class Interface:
    def __init__(self, reference_service):
        self.reference_service = reference_service

    def start(self):
        while True:
            command = input("Enter command: (new, list, exit): ").lower()

            if command == "exit":
                print("Exit selected, goodbye")
                break

            self.command_selector(command)

    def command_selector(self, command):
        if command == "new":
            fields_dict = self.new_reference()
            self.reference_service.save_reference(fields_dict)
        elif command == "list":
         #   print("Not implemented yet")
            return self.reference_service.list_references()

    def new_reference(self):
        fields_dict = self.reference_service.get_template_reference()

        for field in fields_dict:
            user_input = input(f"\t Enter {field}: ")
            fields_dict[field] = user_input

        return fields_dict
