Feature: Users REST API

  @api
  Scenario: Verify the existence of a user
    Given The API "https://jsonplaceholder.typicode.com/users" returns a response of users details
    When There is a GET request to the users endpoint
    Then Verify that user as "Nicholas Runolfsdottir V" exists
    And verify that if this user exists, his address contains the following data
        |  street           |  suite     | city      | zipcode | lat      | lng      |
        |  Ellsworth Summit |  Suite 729 | Aliyaview | 45169   | -14.3990 | -120.7677|