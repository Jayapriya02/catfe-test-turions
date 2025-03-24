Feature: Login Functionality for Parabank

  Scenario: Successful login
    Given the user is on the Parabank login page
    When they enter valid credentials
    Then they should be redirected to the accounts overview page

  Scenario: Invalid login attempt
    Given the user is on the Parabank login page
    When they enter invalid credentials
    Then they should see an error message
