''' Just a simple example of playwright tests.
To run: pytest [--headed] not_reusable.py'''
from playwright.sync_api import Page
from time import sleep
import pytest

# def test_website_after_opening(page: Page):
    # response = page.goto("https://amazon.co.uk")  # visit a website
    # assert response.ok, 'The website does not reply with 2xx'  # check that it has been opened

    # page.locator('id=sp-cc-accept').click()  # cookie accept button
    # actual_text = page.locator('id=nav-link-accountList-nav-line-1').inner_text()  # the Sign in text locator at the website
    # expected_greetings_text = 'Hello, sign in'  # what do we expect at this locator
    # assert actual_text == expected_greetings_text, f'Received: {actual_text}'  # actually test it

    # expected_address_line_one = "Deliver to"  # same with "Deliver to..." lines
    # actual_address_line_one = page.locator('id=glow-ingress-line1').text_content()  
    # assert expected_address_line_one in actual_address_line_one
    # expected_address_line_two = "Finland"
    # actual_address_line_two = page.locator('id=glow-ingress-line2').text_content()
    # assert expected_address_line_two in actual_address_line_two


def test_website_after_search(page: Page):
    page.goto("https://amazon.co.uk")
    page.locator('id=twotabsearchtextbox').fill('book')
    page.locator('id=nav-search-submit-text').click()
    page.locator('id=sp-cc-accept').click()

    actual_text = page.locator('id=Qnav-link-accountList-nav-line-1').inner_text()
    expected_text = 'Hello, sign in'
    assert actual_text == expected_text, f'Received: {actual_text}'

    #sleep(5)
    page.locator('id=s-result-sort-select').select_option('Price: Low to high')  # a price dropdown list
    #sleep(5)
    shown_price = page.locator("xpath=//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]/span[3]").text_content()  # unfortunately XPath is an only option here :(
    assert shown_price == "00"

