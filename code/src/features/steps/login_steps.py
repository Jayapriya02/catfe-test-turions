from playwright.sync_api import sync_playwright
from behave import given, when, then

@given("the user is on the login page")
def step_open_login_page(context):
    context.pw = sync_playwright().start()
    context.browser = context.pw.chromium.launch()
    context.page = context.browser.new_page()
    context.page.goto("https://example.com/login")

@when("they enter valid credentials")
def step_enter_credentials(context):
    context.page.fill("#username", "testuser")
    context.page.fill("#password", "password123")
    context.page.click("#login-button")

@then("they should be redirected to the dashboard")
def step_verify_dashboard(context):
    assert "dashboard" in context.page.url
    context.browser.close()
    context.pw.stop()
