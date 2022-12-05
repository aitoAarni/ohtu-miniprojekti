def command_selector(command, reference_service, user_io):
    if command == "new":
        fields_dict = new_reference(reference_service, user_io)
        reference_service.save_reference(fields_dict)
    elif command == "list":
        list_references(reference_service, user_io)
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
    filter_empty_values = list({key:value for (key, value) in reference.items() if value is not None})
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
        user_input = user_io.input_reference("\t Enter a name for your bib file: ")
        validity = reference_service.check_bib_name_validity(user_input)
    return user_input

def create_bib(reference_service, user_io, file_name):
    reference_service.create_bib(file_name)
    user_io.output_reference("Bib file saved into saved_exports directory\n")


def delete_reference(reference_service, user_io):
    citekey = user_io.input_reference("\t Enter citekey: ")
    reference_service.delete_reference(citekey)
