*** Settings ***
Resource  ../Resources/PO/MainPage.robot
Resource  ../Resources/Common.robot
Test Setup  common.Begin Web Test
Test Teardown  common.End Web Test
Documentation  Open the Vala website and verify the logo


*** Variables ***
${BROWSER} =  chrome
${START_URL} =  https://www.valagroup.com/


*** Test Cases ***
Page elements are visible
    [tags]    smoke
    MainPage.The logo is shown
