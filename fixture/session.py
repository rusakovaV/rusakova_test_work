import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SessionHelper:
    def __init__(self, app):
        self.app = app

    # Нажатие кнопки "Войти" на форме авторизации
    def click_submit(self):
        wd = self.app.wd
        locator = "login-btn"
        with allure.step('Нажать кнопку Войти'):
            wd.find_element(By.CLASS_NAME, f"{locator}").click()

    # Нажатие кнопки "Войти" на форме авторизации с ожиданием подтверждения выхода
    def submit_login(self):
        self.click_submit()
        wd = self.app.wd
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CLASS_NAME, "header__toggle"))

    # Функция авторизации без проверок об успешности
    def wrong_login(self, username, password):
        # На главной страницу нажать кнопку "Войти"
        self.app.main_page.click_button_signin()
        # Заполнить поля email и пароль
        self.fill_auth_fields(username, password)
        # Нажать на кнопку "Войти" в модельном окне "Вход"
        self.click_submit()

    # Функция заполнения полей логина и пароля в модальном окне авторизации "Вход"
    def fill_auth_fields(self, username=None, password=None):
        wd = self.app.wd
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "email").clear()
            wd.find_element(By.NAME, "email").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "password").clear()
            wd.find_element(By.NAME, "password").send_keys(password)

    # Функция авторизации с проверкой успешности
    def login(self, username, password):

        self.app.main_page.click_button_signin()
        self.fill_auth_fields(username, password)
        self.submit_login()

    # Функция проверки сообщения при попытке авторизации с неверным логином
    def check_message_wrong_user(self, expected_message):
        wd = self.app.wd
        with allure.step('Проверка сообщение о некорректном email'):
            actual_message = wd.find_element(By.NAME, "email").get_attribute("validationMessage")
            self.app.assertions.assertion_text(actual_message, expected_message)

    # Функция нажатия на Профиль и выбора пункта "Выйти"
    def init_logout(self):
        wd = self.app.wd
        # Нажать на кнопку Профиль на главной странице
        self.app.main_page.click_button_profile()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.XPATH, "//div[text()='Выйти']"))
        with allure.step('Нажать на Выход'):
            wd.implicitly_wait(2)
            wd.find_element(By.XPATH, "//div[text()='Выйти']").click()

    # Функция логаута
    def logout(self):
        wd = self.app.wd
        self.init_logout()
        # Ожидание кнопки Войти
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CLASS_NAME, "link__signin"))
        with allure.step('Проверка закрытия выпадающего меню пользователя'):
            profile_menu = wd.find_elements(By.CLASS_NAME, "rc-dropdown header_dropdown_items rc-dropdown-placement-bottomRight ")
            assert len(profile_menu) == 0, "Выпадающее меню пользователя не закрыто"









