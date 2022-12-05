*** Settings ***
Library  ../AppLibrary.py

    
*** Keywords *** 
Input Command
    [Arguments]  ${argument}
    Add Input  ${argument}

*** Keywords ***
Output Should Contain Citekey
    [Arguments]  ${citekey}
    Output Should Contain  ${citekey}