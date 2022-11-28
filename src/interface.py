from repositories.reference_repository import default_reference_repository

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
            return self.new_reference()
        elif command == "list":
         #   print("Not implemented yet")
            return self.list_references()

    def new_reference(self):
        citekey = input("\t Enter citekey: ")
        author = input("\t Enter author: ")
        title = input("\t Enter title: ")
        journal = input("\t Enter journal: ")
        year = input("\t Enter year: ")
        volume = input("\t Enter volume: ")
        pages = input("\t Enter pages: ")

        fields_dict = {
            "citekey": citekey,
            "author": author,
            "title": title,
            "journal": journal,
            "year": int(year),
            "volume": volume,
            "pages": pages
        }

        return fields_dict

    def list_references(self):
        references = default_reference_repository.get_all()

        for reference in references:
            print(reference)