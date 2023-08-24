Feature: User can successfully complete purchase of a chosen product

    Background:  The user has successfully logged in
        Given home: I am a user on the Home page
        When home: I login with user standard_user and password secret_sauce
        Then inventory: I should land on the inventory page

@regression
      Scenario: I successfully complete purchase of the item that I have added to cart (backpack)
        When inventory: I  click the backpack add to cart button
        And inventory: I open the shopping cart
        Then shopping_cart_page: I can view the backpack in the shopping cart
        When shopping_cart_page: I click the checkout button
        Then check_out_page1: I should land on the first checkout page
        When check_out_page1: I enter my first name
        And check_out_page1: I enter my last name
        And check_out_page1: I enter my postcode
        And check_out_page1: I click Continue
        Then check_out_page2: I should land on the second checkout page
        When check_out_page2: I click the finish button
        Then checkout_complete_page: I should land on the checkout complete page



