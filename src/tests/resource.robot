*** Settings ***
Library  ../AppLibrary.py



*** Keywords *** 
Input Command
    [Arguments]  ${argument}=${EMPTY}
    Add Input  ${argument}

Add Reference To Database
    Create Reference To Database  serious business  Teppo  lil study  some scrappy one  2000  123456
    Create Reference To Database  citekey02  Sipser  Theory of Computation  Computational Studies  2014  laskennan-mallit