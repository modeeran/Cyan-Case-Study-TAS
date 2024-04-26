@status
Feature: HTTP StatusCodes

  Scenario Outline: Verify the HTTP status code per page
    Given A user goes to the Status Codes page
    When He selects a statusCode link as "<page>" and  navigates to the corresponding sub-page
    Then the correct http statusCode as "<status_code>" should be returned per sub-page
    Examples:
        |  page |  status_code   |
        |  200  |  200           |
        |  301  |  301           |
        |  404  |  404           |
        |  500  |  500           |