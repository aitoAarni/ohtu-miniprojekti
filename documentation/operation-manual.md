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

To store a new reference type in command `new` and press Enter. You will then be guided through a process of filling in entry types for the new reference.

### Browsing references

To browse through stored references type in command `list` and press Enter.

### Deleting references
To delete a reference type in command `delete` and press Enter. Then proceed and enter the citekey of the referense to delete it.

### Editing references
To delete a reference type in command `edit` and press Enter. Then proceed and enter the citekey of the reference to edit it. The new changes replace the old information.

### Importing references
To import references from a bib-tex-file type in command `import` and press Enter. Then proceed and enter name of the file (that has the references) from where to import the references. The command imports all references that are missing from the current file.

### Exporting references
To export the references type in command `export` and press Enter. Then enter the name for the exported file (containing the references).

### Searching references
To search for references containing a specific string type in command `search` and press Enter. Then proceed and enter the string and press Enter. If there are references containing that string they will be listed on the console.

### Exiting the application

Type in `exit` and press Enter to exit the application.


