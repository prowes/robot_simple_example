''' Just a simple example of playwright tests.
To run: pytest [--headed] reusable.py'''
from playwright.sync_api import Page
from time import sleep
import pytest

URL = "https://amazon.co.uk"
COOKIE_CONSENT = "id=sp-cc-accept"
SIGN_IN_TEXT_LOCATOR = "id=nav-link-accountList-nav-line-1"
ADDRESS_LOCATOR_LINE_ONE = "id=glow-ingress-line1"
ADDRESS_LOCATOR_LINE_TWO = "id=glow-ingress-line2"
SEARCH_BAR = "id=twotabsearchtextbox"
SEARCH_BUTTON = "id=nav-search-submit-text"
SORTING_DROPDOWN = "id=s-result-sort-select"
EXPECTED_COUNTRY = "Finland"


def check_sign_in(page): 
    actual_text = page.locator(SIGN_IN_TEXT_LOCATOR).inner_text()  # the Sign in text locator at the website
    expected_greetings_text = 'Hello, sign in'  # what do we expect at this locator
    assert actual_text == expected_greetings_text, f'Received: {actual_text}'  # actually test it


def test_website_after_opening(page: Page):
    response = page.goto(URL)  # visit a website
    assert response.ok, 'The website does not reply with 2xx'  # check that it has been opened

    page.locator(COOKIE_CONSENT).click()  # cookie accept button
    check_sign_in(page)

    expected_address_line_one = "Deliver to"  # same with "Deliver to..." lines
    actual_address_line_one = page.locator(ADDRESS_LOCATOR_LINE_ONE).text_content()  
    assert expected_address_line_one in actual_address_line_one
    actual_address_line_two = page.locator(ADDRESS_LOCATOR_LINE_TWO).text_content()
    assert EXPECTED_COUNTRY in actual_address_line_two


def test_website_after_search(page: Page):
    page.goto(URL)
    page.locator(SEARCH_BAR).fill('book')
    page.locator(SEARCH_BUTTON).click()
    page.locator(COOKIE_CONSENT).click()

    check_sign_in(page)

    sleep(5)
    page.locator(SORTING_DROPDOWN).select_option('Price: Low to high')  # a price dropdown list
    sleep(5)
    shown_price = page.locator("xpath=//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]/span[2]").text_content()  # unfortunately XPath is an only option here :(
    assert shown_price == "0."

