@login
Feature: Form Authentication

  Scenario: Successful authentication
    Given A user goes to the login page
    When He adds a valid username as "tomsmith" and password as "SuperSecretPassword!" in the form
    And He clicks on the login button
    Then He should be logged in to the system - the message of "You logged into a secure area!" should be displayed


  Scenario: Unsuccessful authentication with an invalid username
    Given A user goes to the login page
    When He adds an invalid username as "invalid_user" and a valid password as "SuperSecretPassword!" in the form
    And He clicks on the login button
    Then System displays a failed validation message for username - "Your username is invalid!"


  Scenario: Unsuccessful authentication with an invalid password
    Given A user goes to the login page
    When He adds a valid username as "tomsmith" and an invalid password as "123" in the form
    And He clicks on the login button
    Then System displays a failed validation message for password - "Your password is invalid!"


  Scenario: Unsuccessful authentication when the form is not filled out
    Given A user goes to the login page
    When He clicks on the login button
    Then System displays a failed validation message for username - "Your username is invalid!"