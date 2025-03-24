import pytest
from playwright.sync_api import sync_playwright

# Test Data
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
VALID_USERNAME = "john"
VALID_PASSWORD = "demo"
INVALID_PASSWORD = "wrong_password"

@pytest.fixture(scope="function")
def browser():
    """Setup Playwright browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_valid_login(browser):
    """Test valid user login"""
    browser.goto(BASE_URL)
    browser.fill("input[name='username']", VALID_USERNAME)
    browser.fill("input[name='password']", VALID_PASSWORD)
    browser.click("input[value='Log In']")
    
    assert browser.locator("text=Accounts Overview").is_visible()

def test_invalid_login(browser):
    """Test invalid user login"""
    browser.goto(BASE_URL)
    browser.fill("input[name='username']", VALID_USERNAME)
    browser.fill("input[name='password']", INVALID_PASSWORD)
    browser.click("input[value='Log In']")
    
    assert browser.locator("text=Error!").is_visible()
