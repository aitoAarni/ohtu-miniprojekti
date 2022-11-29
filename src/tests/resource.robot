*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Commands
    Input  value

Clear Inputs
    Clear Inputs



Choose Operation
    [Arguments]  ${operation}
    Add Input  ${operation}