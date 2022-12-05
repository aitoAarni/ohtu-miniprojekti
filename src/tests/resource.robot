*** Settings ***
Library  ../AppLibrary.py

    
*** Keywords *** 
Input Command
    [Arguments]  ${argument}
    Add Input  ${argument}

Add Reference To Database
    Create Reference To Database  serious business  Teppo  lil study  some scrappy one  2000