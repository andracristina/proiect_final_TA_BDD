from pages.checkout_complete_page import CheckoutCompletePage

checkout_complete_page = CheckoutCompletePage()

@then('checkout_complete_page: I should land on the checkout complete page')
def step_impl(context):
    checkout_complete_page.validate_correct_url()


@when('checkout_complete_page: I press the Back Home button')
def step_impl(context):
    checkout_complete_page.click_back_home_button()


