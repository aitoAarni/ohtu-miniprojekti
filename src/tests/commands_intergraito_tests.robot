*** Settings ***
Resource  resource.robot
Test Setup  Delete All Records From Database

*** Test Cases ***
Add Reference
    Input Command  new
    Input Command  citekeyValue
    Input Command  authorValue
    Input Command  title1Value
    Input Command  journal1Value
    Input Command  1900
    Input Command
    Input Command  exit
    Run Application
    Output Should Contain Citekey  citekeyValue

Delete Reference
    Add Reference To Database
    Input Command  delete
    Input Command  serious business
    Input Command  exit
    Run Application  
    Output Should Be Empty

Edit Reference
    Add Reference To Database
    Input Command  edit
    Input Command  serious business
    Input Command  Me
    Input Command  CEO
    Input Command  my diary
    Input Command  2022
    Input Command
    Input Command  exit
    Run Application
    Edited Output Should Contain  serious business  Me  CEO  my diary  2022


*** Keywords ***
Output Should Contain Citekey
    [Arguments]  ${citekey}
    Output Should Contain  ${citekey}

Edited Output Should Contain
    [Arguments]  @{args}
    Output Should Contain  @{args}