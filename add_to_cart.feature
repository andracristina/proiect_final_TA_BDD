Feature: User can successfully add the backpack item to cart

    Background:  The user has successfully logged in
        Given home: I am a user on the Home page
        When home: I login with user standard_user and password secret_sauce
        Then inventory: I should land on the inventory page

    @smoke
    Scenario: I successfully add the backpack item to cart from the Inventory page
        Given inventory: I am on the inventory page
        When inventory: I  click the backpack add to cart button
        And inventory: I open the shopping cart
        Then shopping_cart_page: I can view the backpack in the shopping cart

