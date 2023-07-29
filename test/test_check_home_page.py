import allure

@allure.epic("Набор тестов по проверке отображения страниц")
@allure.description("Проверка отображения главной страницы")
def test_check_home_page(app):

    # Открыть главную страницу
    app.open_home_page()
    # Если пользователь авторизован выполнить логаут
    if app.main_page.find_button_profile() == 1:
        app.session.logout()

    # Проверить элементы на странице
    app.main_page.check_main_menu_without_auth()






