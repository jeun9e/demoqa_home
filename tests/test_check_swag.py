from pages.swag_labs import SwagLabs

# тест кейс, проверка наличия элемента на странице, поля имени и поля пароля
def test_case(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon()
    assert swag_page.user_name()
    assert swag_page.user_password()
