from collections import defaultdict


def command_selector(command, reference_service, user_io):
    if command == "new":
        fields_dict = new_reference(reference_service, user_io)
        reference_service.save_reference(fields_dict)
    elif command == "list":
        list_references(reference_service, user_io)
    elif command == "edit":
        edit_reference(reference_service, user_io)
    elif command == 'import':
        file_name = select_importable_file(reference_service, user_io)
        import_file(file_name, reference_service, user_io)
    elif command == "export":
        file_name = create_name_for_bib(reference_service, user_io)
        create_bib(reference_service, user_io, file_name)
    elif command == "delete":
        delete_reference(reference_service, user_io)
    elif command == "search":
        search_references_with_given_string(reference_service, user_io)
    else:
        user_io.output_reference("Command not found")


def new_reference(reference_service, user_io):
    fields_dict = reference_service.get_template_reference()
    required_fields_list = reference_service.get_required_fields()
    optional_fields_list = reference_service.get_optional_fields()
    print_header("ADD A NEW REFERENCE", user_io)

    for field in required_fields_list:
        user_input = user_io.input_reference(f"Enter {field}: ")
        validity = reference_service.check_data_validity(field, user_input)
        while validity is not True:
            user_io.output_reference(validity)
            user_input = user_io.input_reference(f"Enter {field}: ")
            validity = reference_service.check_data_validity(field, user_input)
        fields_dict[field] = user_input

    for field in optional_fields_list:
        user_input = user_io.input_reference(f"Enter {field}: ")
        if len(user_input):
            fields_dict[field] = user_input

    user_io.output_reference(f"\nCitekey {fields_dict['citekey']} added")
    return fields_dict

def list_references(reference_service, user_io):
    references = reference_service.get_all_references()

    print_header("LIST OF SAVED REFERENCES", user_io)

    for reference in references:
        print_reference_objects(reference, user_io)

    return references


def print_reference_objects(reference, user_io):
    filter_empty_values = list(
        {key: value for (key, value) in reference.items() if value is not None})
    last_key = list(filter_empty_values)[-1]

    for key, value in reference.items():
        if not value:
            continue

        if key == "citekey":
            user_io.output_reference(f"{key}: {value}")
            user_io.output_reference("")
        elif key == last_key:
            user_io.output_reference(f"  └── {key}: {value}")
        else:
            user_io.output_reference(f"  ├── {key}: {value}")
    user_io.output_reference("")

def print_header(header, user_io):
    user_io.output_reference("-" * len(header))
    user_io.output_reference(header)
    user_io.output_reference("-" * len(header))
    user_io.output_reference("")

def create_name_for_bib(reference_service, user_io):
    print_header("EXPORT SAVED REFERENCES TO A FILE", user_io)
    user_input = user_io.input_reference("Enter a name for your bib file: ")
    validity = reference_service.check_bib_name_validity(user_input)
    while validity is not True:
        user_io.output_reference(validity)
        user_input = user_io.input_reference(
            "Enter a name for your bib file: ")
        validity = reference_service.check_bib_name_validity(user_input)
    return user_input


def create_bib(reference_service, user_io, file_name):
    reference_service.create_bib(file_name)
    user_io.output_reference("\nBib file saved into saved_exports directory")


def delete_reference(reference_service, user_io):
    print_header("DELETE A REFERENCE", user_io)
    user_input = user_io.input_reference("Enter citekey: ")
    result = reference_service.delete_reference_by_citekey(user_input)
    if not result:
        user_io.output_reference("\nNothing deleted")
    else:
        user_io.output_reference(f"\nEntry {result} deleted")


def edit_reference(reference_service, user_io):
    user_io.output_reference(
        "Edit reference selected, select a citekey to edit: \n")
    list_references(reference_service, user_io)
    citekey_input = user_io.input_reference("Enter a citekey: ")
    reference = reference_service.get_reference(citekey_input)

    while not reference:
        citekey_input = user_io.input_reference("Invalid citekey, try again: ")
        reference = reference_service.get_reference(citekey_input)

    reference = filter_out_empty_fields(reference)
    fields = list(reference.keys())

    user_io.output_reference(
        f"\nEnter new fields for citekey {reference['citekey']} (press ENTER to skip fieldx): \n")

    result_reference = defaultdict(lambda: "")

    for field in fields:
        if field == "citekey":
            result_reference[field] = reference[field]
        while not result_reference[field]:
            user_input = user_io.input_reference(
                f"Enter new value for {field}: ")
            if user_input:
                result_reference[field] = user_input
            else:
                result_reference[field] = reference[field]

    result = reference_service.edit_reference(result_reference)
    result_dict = result.get_fields()

    print("")
    if result:
        user_io.output_reference(f"Reference {result_dict['citekey']} updated")
    else:
        user_io.output_reference("Error: Reference not updated!")


def filter_out_empty_fields(reference):
    filter_empty_values = {key: value for (
        key, value) in reference.items() if value is not None}
    return filter_empty_values


def select_importable_file(reference_service, user_io):
    print_header("IMPORT REFERENCES FROM A FILE", user_io)
    importable_files = reference_service.get_importable_files()
    user_io.output_reference("Importable files (from imports directory):")
    for file in importable_files:
        user_io.output_reference(f'{file}')
    selected_file = user_io.input_reference('\nEnter file to be imported: ')
    if selected_file not in importable_files:
        user_io.output_reference("File not found \n")
        return False
    return selected_file


def import_file(file_name, reference_service, user_io):
    if not file_name:
        return

    imported_citekeys = reference_service.import_file(file_name)
    user_io.output_reference('\nImported citekeys:')
    for citekey in imported_citekeys:
        user_io.output_reference(f'{citekey}')
    if not imported_citekeys or imported_citekeys == []:
        user_io.output_reference('None')


def search_references_with_given_string(reference_service, user_io):
    print_header("SEARCH FROM REFERENCES", user_io)
    user_input = user_io.input_reference("Search with string: ")
    result = reference_service.search_references_with_string(user_input)
    user_io.output_reference("")
    if not result:
        user_io.output_reference("No references containing that string")
    else:
        print_header(f'Search results matching keyword "{user_input}":', user_io)
        for reference in result:
            print_reference_objects(reference, user_io)
