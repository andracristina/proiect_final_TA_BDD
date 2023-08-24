Feature: Login capability

  Background: I am a user on the Home page
    Given home: I am a user on the Home page

  @regression
  Scenario: Successful login - I login with valid credentials
    When home: I login with user standard_user and password secret_sauce
    Then inventory: I should land on the inventory page


  @regression
  Scenario Outline: I attempt login with invalid credentials
    When home: I login with user <user> and password <password>
    Then home: I validate the correct invalid credentials error message is displayed

    Examples:

    | user            | password      |
    | standard_user   | 123Test       |
    | user_standard   | secret_sauce  |


  @regression
  Scenario: I attempt login with locked out credentials
    When home: I login with user locked_out_user and password secret_sauce
    Then home: I validate the correct locked out credentials error message is displayed


