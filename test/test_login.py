import pytest
import allure

@allure.epic("Набор тестов авторизации")
@pytest.mark.parametrize("username, password", [("test_rusakova@internet.ru", "84426369"), ("test", "test")])
def test_login(app, username, password):

    # Открыть главную страницу
    app.open_home_page()

    # Предусловие: если пользователь залогинен, выполнить логаут
    if app.main_page.find_button_profile()== 1:
        app.session.logout()

    # Если данные корректны
    if username == "test_rusakova@internet.ru" and password == "84426369":
        # Выполнить вход в УЗ
        app.session.login(username=username, password=password)
        # Проверить наличие кнопки профиль
        assert app.main_page.find_button_profile()== 1, "Кнопка Профиль не найдена"

    # Если данные УЗ некорретны
    else:
        # Выполнить попытку входа
        app.session.wrong_login(username=username, password=password)
        # Проверить всплывающее сообщение об ошибке
        expected_message = "Адрес электронной почты должен содержать символ \"@\". В адресе \"test\" отсутствует символ \"@\"."
        app.session.check_message_wrong_user(expected_message)
