Feature: Login capability

  Background: I am a user on the Home page
    Given home: I am a user on the Home page

  @smoke
  Scenario: Successful login - I login with valid credentials
    When home: I login with user standard_user and password secret_sauce
    Then inventory: I should land on the inventory page

  @smoke
  Scenario: I attempt login with invalid credentials
    When home: I login with user standard_user and password 123Test
    Then home: I validate the correct invalid credentials error message is displayed