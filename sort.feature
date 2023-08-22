Feature: User can successfully sort the available items by different criteria


    Background:  The user has successfully logged in
      Given home: I am a user on the Home page
      When home: I login with user standard_user and password secret_sauce


  @regression

    Scenario: I am able to sort the product list in reverse alphabetical order (Z to A)
      Given inventory: I am on the inventory page
      When inventory: I click the sorting drop-down menu
      And inventory: I select Name (Z to A) option
      Then inventory: I validate that the products are arranged in reverse alphabetical order


