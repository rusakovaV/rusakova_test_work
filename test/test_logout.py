import allure
import pytest

@allure.epic("Набор тестов выхода из учетной записи")
@allure.description("Выход из учетной записи")
@pytest.mark.parametrize("username, password", [("test_rusakova@internet.ru", "84426369")])
def test_logout(app, username, password):

    app.open_home_page()
    # Если пользователь авторизован, выполнить логаут
    if app.main_page.find_button_profile()== 1:
        app.session.logout()

    else:
        # Если пользователь не авторизован выполнить логин и затем логаут
        app.session.login(username=username, password=password)
        app.session.logout()

