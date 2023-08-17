Feature: Login capability with valid credentials

  @regression

  Scenario: Successful login - I login with valid credentials
    Given home: I am a user on the Home page
    When home: I enter my username
    And home: I enter my password
    And home: I click the login button
    Then inventory: I should land on the inventory page