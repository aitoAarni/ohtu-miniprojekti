from ui.commands import command_selector

class Interface:
    def __init__(self, reference_service, user_input):
        self.reference_service = reference_service
        self.user_io = user_input

    def start(self):
        while True:
            command = self.user_io.input_reference(
                "Enter command: (new, list, edit, export, delete, exit): ").lower()

            if command == "exit":
                self.user_io.output_reference("Exit selected, goodbye")
                return "Exit selected, goodbye"

            print("")
            command_selector(command, self.reference_service, self.user_io)
