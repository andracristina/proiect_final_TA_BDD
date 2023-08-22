Feature: Logout capability

  Background: I am a logged in user on the Inventory page
    Given home: I am a user on the Home page
    When home: I login with user standard_user and password secret_sauce
    Then inventory: I should land on the inventory page

    @logoutinprogress

    Scenario: I am able to successfully log out of my account
      Given inventory: I am on the inventory page
      When inventory: I click the menu button
      When inventory: I click the logout button
      Then home: I should land on the home page
