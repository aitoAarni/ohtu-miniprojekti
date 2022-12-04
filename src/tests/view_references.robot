*** Settings ***
Resource  resource.robot
Test Setup  Delete Records From Database

*** Test Cases ***
View All References
    Add Reference
    Choose Operation  list
    Run Application
    Output Should Contain    

*** Keywords ***
Choose Operation
    [Arguments]  ${operation}
    Add Input  ${operation}

Add Reference Field
    [Arguments]  ${argument}
    Add Reference Input  ${argument}

Add Reference
    Choose Operation  new
    Add Reference Field  citekey
    Add Reference Field  author
    Add Reference Field  title1
    Add Reference Field  journal1
    Add Reference Field  1900
    Run Application
    Output Should Contain    