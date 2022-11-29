*** Settings ***
Resource resource.robot


*** Keywords ***
Choose Operation
    [Arguments]  ${operation}
    Input  ${operation}