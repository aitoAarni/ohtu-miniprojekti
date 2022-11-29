*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Commands
    Input  value

Clear Inputs
    Clear Inputs


Print Debugger
    [Arguments]  ${message}
    Print Message  ${message}