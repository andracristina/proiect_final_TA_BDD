Feature: Login capability

  Background: I am a user on the Home page
    Given home: I am a user on the Home page

  @smoke
  Scenario: Successful login - I login with valid credentials
    When home: I login with user standard_user and password secret_sauce
    Then inventory: I should land on the inventory page


  @negative
  Scenario Outline: I attempt login with invalid credentials
    When home: I login with user <user> and password <password>
    Then home: I validate the correct invalid credentials error message is displayed

    Examples:

    | user            | password      |
    | standard_user   | 123Test       |
    | user_standard   | secret_sauce  |



