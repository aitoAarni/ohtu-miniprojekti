*** Settings ***
Resource  resource.robot
Test Setup  Delete All Records From Database
Test Teardown  Delete Exported And Imported Files

*** Test Cases ***
As A User I Can Add A Reference With Authors Title Year And Journal
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

As A User I Can List Stored References
    Add Reference To Database
    Input Command  list
    Input Command  exit
    Run Application
    Output Contains  citekey02

As A User I Can Export Stored References
    Add Reference To Database
    Input Command  export
    Input Command  robot-test
    Input Command  exit
    Run Application
    Output Contains  Bib file saved into


As A User I Can Delete A Reference
    Add Reference To Database
    Input Command  delete
    Input Command  serious business
    Input Command  delete
    Input Command  citekey02
    Input Command  exit
    Run Application  
    Output Should Be Empty

As A User I Can Edit A Reference
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

As A User I Can Search References With A Given Word
    Add Reference To Database
    Input Command  search
    Input Command  2000
    Input Command  exit
    Run Application
    Edited Output Should Contain  serious business  Teppo  lil study  some scrappy one  2000

As A User I Can Search References With A Tag
    Add Reference To Database
    Input Command  search
    Input Command  laskennan-mallit
    Input Command  exit
    Run Application
    Output Should Contain  citekey02

As A User I Can Import References From A File
    Create Bib File For Robot Test 
    Add Reference To Database
    Input Command  import
    Input Command  robot-test.bib
    Input COmmand  exit
    Run Application
    Output Contains  testcormen01

*** Keywords ***
Output Should Contain Citekey
    [Arguments]  ${citekey}
    Output Should Contain  ${citekey}

Edited Output Should Contain
    [Arguments]  @{args}
    Output Should Contain  @{args}