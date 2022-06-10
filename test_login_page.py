from .pages.login_page import LoginPage


def test_guest_can_see_all_required_elements_on_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()          
