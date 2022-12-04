*** Settings ***
Resource  resource.robot
Test Setup  Delete Records From Database

*** Test Cases ***
Add Reference
    Choose Operation  new
    Add Reference Field  citekey
    Add Reference Field  author
    Add Reference Field  title1
    Add Reference Field  journal1
    Add Reference Field  1900
    Run Application
    Output Should Contain    

*** Keywords ***

Add Reference Field
    [Arguments]  ${argument}
    Add Reference Input  ${argument}


