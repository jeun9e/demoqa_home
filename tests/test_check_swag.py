from pages.swag_labs import SwagLabs


def test_icon(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    swag_page.click_on_the_icon()
    assert swag_page.exist_icon()
    assert swag_page.user_name()
    assert swag_page.user_password()
