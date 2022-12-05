*** Settings ***
Resource  resource.robot
Test Setup  Delete Records From Database

*** Test Cases ***
Add Reference
    Input Command  new
    Input Command  citekeyValue
    Input Command  authorValue
    Input Command  title1Value
    Input Command  journal1Value
    Input Command  1900
    Input Command  exit
    Run Application
    Output Should Contain Citekey  citekeyValue

Delete Reference
    Add Reference To Database  reference
    Input Command  delete
    Input Command  reference
    Input Command  exit
    Run Application  
    Output Should Be Empty
