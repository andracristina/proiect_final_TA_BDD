Feature: User can successfully sort the available items by different criteria



    Background:  The user has successfully logged in
        Given home: I am a user on the Home page
        When home: I enter my username
        And home: I enter my password
        And home: I click the login button
        Then inventory: I should land on the inventory page

  @inprogress

    Scenario: I am able to sort the product list in reverse alphabetical order (Z to A)
      Given inventory: I am on the inventory page
      When inventory: I click the sorting drop-down menu
      And inventory: I select Name (Z to A) option


