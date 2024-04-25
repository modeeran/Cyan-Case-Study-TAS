Feature: Form Authentication

  @login2
  Scenario: Successful authentication
    Given A user goes to the login page
    When He adds a valid username as "tomsmith" and password as "SuperSecretPassword!" in the form
    And He clicks on the login button
    Then He should be logged in to the system


  @login
  Scenario: Unsuccessful authentication with an invalid username
    Given A user goes to the login page
    When He adds an invalid username as "invalid_user" and a valid password as "SuperSecretPassword!" in the form
    And He clicks on the login button
    Then The system should display a failed authentication validation message - Your username is invalid!

  @login
  Scenario: Unsuccessful authentication with an invalid password
    Given A user goes to the login page
    When He adds a valid username as "tomsmith" and an invalid password as "123" in the form
    And He clicks on the login button
    Then The system should display a failed authentication validation message - Your password is invalid!


  @login
  Scenario: Unsuccessful authentication when the form is not filled out
    Given A user goes to the login page
    When He does not add any credentials in the form
    And He clicks on the login button
    Then The system should display a failed authentication validation message - Your username is invalid!