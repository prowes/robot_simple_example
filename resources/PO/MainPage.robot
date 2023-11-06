*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${VALA_LOGO} =  class=logo--header


*** Keywords ***
The logo is shown
    Wait Until Element Is Visible  ${VALA_LOGO}
