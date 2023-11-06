*** Settings ***
Library  SeleniumLibrary


*** Keywords ***
Begin Web Test
    Open Browser  about:blank  ${BROWSER}
    Go To  ${START_URL}
    Maximize Browser Window


End Web Test
    Close Browser