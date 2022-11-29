*** Settings ***
Resource resource.robot
Test Setup  Clear Database And Inputs


*** Test Cases ***
Add Reference
    Choose Operation  new
    Input  citekey
    Input  author
    Input  title
    Run Application


*** Keywords ***
Choose Operation
    [Arguments]  ${operation}
    Input  ${operation}

Clear Database And Inputs
    Initialize Test

