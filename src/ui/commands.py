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


def new_reference(reference_service, user_io):
    fields_dict = reference_service.get_template_reference()
    required_fields_list = reference_service.get_required_fields()

    for field in required_fields_list:
        user_input = user_io.input_reference(f"\t Enter {field}: ")
        validity = reference_service.check_data_validity(field, user_input)
        while validity is not True:
            user_io.output_reference(validity)
            user_input = user_io.input_reference(f"\t Enter {field}: ")
            validity = reference_service.check_data_validity(field, user_input)
        fields_dict[field] = user_input

    return fields_dict


def list_references(reference_service, user_io):
    references = reference_service.get_all_references()

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
            user_io.output_reference(f"{key} {value}")
        elif key == last_key:
            user_io.output_reference(f"  └── {key}: {value}")
        else:
            user_io.output_reference(f"  ├── {key}: {value}")
    user_io.output_reference("\n")


def create_name_for_bib(reference_service, user_io):
    user_input = user_io.input_reference("\t Enter a name for your bib file: ")
    validity = reference_service.check_bib_name_validity(user_input)
    while validity is not True:
        user_io.output_reference(validity)
        user_input = user_io.input_reference(
            "\t Enter a name for your bib file: ")
        validity = reference_service.check_bib_name_validity(user_input)
    return user_input


def create_bib(reference_service, user_io, file_name):
    reference_service.create_bib(file_name)
    user_io.output_reference("Bib file saved into saved_exports directory\n")


def delete_reference(reference_service, user_io):
    user_input = user_io.input_reference("\t Enter citekey: ")
    result = reference_service.delete_reference_by_citekey(user_input)
    if not result:
        user_io.output_reference("Nothing deleted\n")
    else:
        user_io.output_reference("Entry deleted\n")


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
        f"\nEnter new fields for citekey {reference['citekey']} (press ENTER to skip field): \n")

    result_reference = defaultdict(lambda: "")

    for field in fields:
        if field == "citekey":
            result_reference[field] = reference[field]
        while not result_reference[field]:
            input = user_io.input_reference(f"Enter new value for {field}: ")
            if input:
                result_reference[field] = input
            else:
                result_reference[field] = reference[field]

    result = reference_service.edit_reference(result_reference)
    result_dict = result.get_fields()

    print("")
    if result:
        user_io.output_reference(f"Reference {result_dict['citekey']} updated")
    else:
        user_io.output_reference("Error: Reference not updated!")
    print("")


def filter_out_empty_fields(reference):
    filter_empty_values = {key: value for (
        key, value) in reference.items() if value is not None}
    return filter_empty_values


def select_importable_file(reference_service, user_io):
    importable_files = reference_service.get_importable_files()
    user_io.output_reference("Importable files (from imports directory):")
    for file in importable_files:
        user_io.output_reference(f'{file}')
    selected_file = user_io.input_reference('\n\t Enter file to be imported: ')
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
    user_io.output_reference('')
