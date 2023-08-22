Feature: Inventory capability

    Background:  The user has successfully logged in
        Given home: I am a user on the Home page
        When home: I login with user standard_user and password secret_sauce

@inventory
      Scenario: I validate the product count in the inventory
        Then inventory: I validate that 6 products are displayed

      Scenario: I validate that correct products are displayed




