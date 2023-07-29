import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from fixture.session import SessionHelper
from fixture.main_page import MainPageHelper
from fixture.assertions import AssertionsHelper


class Application:
    def __init__(self, browser, base_url):

        # Возможность указывать в каком браузере запускать тесты из консоли

        #if browser == "firefox": self.wd = webdriver.Firefox()
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        #elif browser == "ie": self.wd = webdriver.Ie()
        else:
            raise ValueError("Не указан браузер")


        self.vars = {}
        self.session = SessionHelper(self)
        self.main_page = MainPageHelper(self)
        self.base_url = base_url
        self.assertions = AssertionsHelper(self)

    def destroy(self):
        self.wd.quit()

    # Функция открытия главной страницы
    def open_home_page(self):
        with allure.step('Открытие страницы SQL Academy'):
            self.wd.get(self.base_url)
        a= 1662
        b=1226
        with allure.step(f'Открытие окна браузера в размере {a}x{b}'):
            self.wd.set_window_size(a, b)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
