# Manual

## Installation

Download the project from Github. Use the following commands to install the application:

```
poetry install
```

```
poetry run invoke build
```

## Launching the application

Launch the application with the following command

```
poetry run invoke start
```

## User Guide

### Storing references

To store a new reference type in command `new` and press Enter. You will then be guided through a process of filling in entry types for the new reference. You can leave some fields empty simply by pressing enter.

### Browsing references

To browse through stored references type in command `list` and press Enter.

### Deleting references
To delete a reference type in command `delete` and press Enter. Then proceed and enter the citekey of the referense to delete it.

### Editing references
To delete a reference type in command `edit` and press Enter. Then proceed and enter the citekey of the reference to edit it. The new changes replace the old information.

### Exporting references
To export the references type in command `export` and press Enter. Then enter the name for the exported file (containing the references).

### Exiting the application

Type in `exit` and press Enter to exit the application.

