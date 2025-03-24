from behave import given, when, then
from playwright.sync_api import sync_playwright

@given("User is on the Parabank login page")
def step_impl(context):
    context.browser = sync_playwright().start().chromium.launch()
    context.page = context.browser.new_page()
    context.page.goto("https://parabank.parasoft.com/")

@when('User enters "{username}" as username and "{password}" as password')
def step_impl(context, username, password):
    context.page.fill("input[name='username']", username)
    context.page.fill("input[name='password']", password)
    context.page.click("input[type='submit']")

@then("User should see the dashboard")
def step_impl(context):
    assert "Accounts Overview" in context.page.inner_text("#rightPanel")
    context.browser.close()
