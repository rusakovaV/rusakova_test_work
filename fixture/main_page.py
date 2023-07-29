
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPageHelper:


    def __init__(self, app):
        self.app = app

    # Функция проверки наличия кнопки "Войти" и возвращения результата
    def find_button_profile(self):
        wd = self.app.wd
        locator = "//div[@class='header__auth']//div[@class='profile__icon']"
        with allure.step('Проверка наличия кнопки профиля'):
            button = len(wd.find_elements(By.XPATH, f"{locator}"))
            return button


    # Функция открытия выпадающего меню управления пользователем
    def open_profile_menu(self):
        wd = self.app.wd
        with allure.step('Нажать на иконку профиля'):
            wd.find_element(By.CLASS_NAME, "header__toggle").click()
        with allure.step('Ожидание открытия выпадающего меню профиля'):
            WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CLASS_NAME,
                                                                 "rc-dropdown header_dropdown_items rc-dropdown-placement-bottomRight "))
    # Функция проверки наличия иконки профиля
    def check_button_profile(self):
        wd = self.app.wd
        with allure.step('Проверка наличия иконки профиля'):
            icon = wd.find_elements(By.XPATH, "//div[@class='header__toggle']//img[@alt='avatar']")
            self.app.assertions.assertion_count_elements(icon)

    # Функция проверки наличия кнопки "Войти"
    def check_button_singin(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки "Войти"'):
            button = wd.find_elements(By.CLASS_NAME, "link__signin")
            self.app.assertions.assertion_count_elements(button)

    # Функция нажатия на профиль
    def click_button_profile(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку профиля'):
            wd.find_element(By.CLASS_NAME, "header__toggle").click()
        with allure.step('Ожидание открытия выпадающего меню'):
            WebDriverWait(wd, 20).until(lambda x: x.find_element(By.CSS_SELECTOR, ".rc-dropdown.header_dropdown_items.rc-dropdown-placement-bottomRight "))

    # Функция нажатия на кнопку "Войти"
    def click_button_signin(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку "Войти'):
            wd.find_element(By.CLASS_NAME, "link__signin").click()
        with allure.step('Ожидание открытия модального окна "Вход"'):
            WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CLASS_NAME, "title"))

    # Функция проверки элементов главной страницы
    def check_main_menu_without_auth(self):
        self.check_button_logo()
        self.check_button_guide()
        self.check_button_trainer()
        self.check_button_more()
        self.check_func_search()
        self.check_button_premium()
        self.check_button_singin()
        self.check_title()
        self.check_module_sql()
        self.check_guide_plane()
        self.check_tasks_plane()
        self.check_statistic()
        self.check_button_join()
        self.check_social_vk()
        self.check_social_email()
        self.check_terms_of_use()
        self.check_button_lang()

    # Функция проверки наличия кнопки с логотипом
    def check_button_logo(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки с логотипом'):
            button = wd.find_elements(By.XPATH, "//div[@class='content']//div[@class='header__logo']")
            assert len(button) == 1, "Кнопка с логотипом не найдена"

    # Функция проверки наличия кнопки Курс
    def check_button_guide(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки Курс'):
            button = wd.find_elements(By.XPATH, "//div[@class='content']//span[contains(.,'Курс')]")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия кнопки Тренажёр
    def check_button_trainer(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки Тренажёр'):
            button = wd.find_elements(By.XPATH, "//div[@class='content']//span[contains(.,'Тренажёр')]")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия кнопки Ещё
    def check_button_more(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки Ещё'):
            button = wd.find_elements(By.XPATH, "//div[@class='nav-links']//div[contains(.,'Ещё')]")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия элемента "Поиск по функции"
    def check_func_search(self):
        wd = self.app.wd
        with allure.step('Проверка наличия Поиска по функции'):
            button = wd.find_elements(By.XPATH, "//div[@class='header__rightbar']//div[@class='sc-1209ff1f-0 dFkSaV']")
            self.app.assertions.assertion_count_elements(button)
        with allure.step('Проверка наличия лупы'):
            button = wd.find_elements(By.CSS_SELECTOR, ".svg-inline--fa.fa-magnifying-glass ")
            self.app.assertions.assertion_count_elements(button)
        with allure.step('Проверка наличия иконки ctrl'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1209ff1f-0 dFkSaV']/div[contains(.,'ctrl')]")
            self.app.assertions.assertion_count_elements(button)
        with allure.step('Проверка наличия иконки K'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1209ff1f-0 dFkSaV']/div[contains(.,'K')]")
            self.app.assertions.assertion_count_elements(button)
        with allure.step('Проверка наличия названия поля поиска'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1209ff1f-0 dFkSaV']/input[@placeholder='Поиск по функциям']")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия кнопки "Премиум"
    def check_button_premium(self):
        wd = self.app.wd
        with allure.step('Проверка наличия кнопки Премиум'):
            button = wd.find_elements(By.CSS_SELECTOR, ".nav-item.premium-nav-item")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия динамического заголовка страницы
    def check_title(self):
        wd = self.app.wd
        with allure.step('Проверка наличия динамического заголовка страницы'):
            button = wd.find_elements(By.CSS_SELECTOR, "div.sc-1b9df9ab-5.BWklI")
            self.app.assertions.assertion_count_elements(button)

    # Функция проверки наличия блоков Курс по SQL, Тренажёр с задачами, Песочница
    def check_module_sql(self):
        wd = self.app.wd
        with allure.step('Проверка наличия блока Курс по SQL'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1b9df9ab-6 ctaWkX']/a[@class='sc-1b9df9ab-10 sc-1b9df9ab-12 eZUxSy jrBOgl']")
            self.app.assertions.assertion_count_elements(button)

        with allure.step('Проверка наличия блока Тренажёр с задачами'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1b9df9ab-6 ctaWkX']/a[@class='sc-1b9df9ab-10 sc-1b9df9ab-13 eZUxSy jdofWT']")
            self.app.assertions.assertion_count_elements(button)

        with allure.step('Проверка наличия блока Песочница'):
            button = wd.find_elements(By.XPATH, "//div[@class='sc-1b9df9ab-6 ctaWkX']/a[@class='sc-1b9df9ab-10 sc-1b9df9ab-15 eZUxSy bCPwcA']")
            self.app.assertions.assertion_count_elements(button)


    # Функция проверки наличия блока "Получи необходимые знания по SQL на нашем бесплатном курсе" с описанием
    def check_guide_plane(self):
        wd = self.app.wd
        locator = "//div[@class='sc-1b9df9ab-16 gVrypE']//div[@class='sc-1b9df9ab-18 iPKjtS']"
        with allure.step('Проверка наличия заголовка плана'):
            title = wd.find_elements(By.XPATH, locator)
            self.app.assertions.assertion_count_elements(title)
        with allure.step('Проверка текста заголовка плана'):
            actual_text = wd.find_element(By.XPATH, locator).get_attribute("textContent")
            expected_text = "Получи необходимые знания по SQL на нашем бесплатном курсе"
            self.app.assertions.assertion_text(actual_text, expected_text)

        locator = "//div[@class='sc-1b9df9ab-16 gVrypE']//div[@class='sc-e3860b72-5 evNBRT']"
        with allure.step('Проверка наличия блока плана курса'):
            plane = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(plane)
        with allure.step('Проверка описания плана курса'):
            actual_text = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_text = "Модуль 0ВведениеВ этом коротком модуле мы познакомимся с тем как работает платформа данного курса и узнаем как получить максимум от него. " \
                            "А также получим информацию о нашем сообществе.ВведениеСтруктура курсаСообществоМодуль 1Фундаментальные основыЭто модуль сделан, чтобы бегло " \
                            "ознакомиться с фундаментальными знаниями о базах данных и восполнить потенциальные пробелы. Также в этом модуле мы познакомимся с " \
                            "терминологией реляционных СУБД.Базы данных и СУБДТипы баз данныхРеляционные базы данныхKey-value базы данныхДокументоориентированные " \
                            "базы данныхСтруктура реляционных баз данныхВводная информация о SQLМодуль 2Основы выборки IВ рамках этого модуля мы научимся писать " \
                            "наши первые SQL запросы, разбиремся с такими важными понятиями как условная выборка, сортировка и группировка данных.Базовый синтаксис " \
                            "SQL запросаЛитералыПрименение функцийИсключение дубликатов, DISTINCTУсловный оператор WHEREОператоры IS NULL, BETWEEN, INОператор " \
                            "LIKEСортировка, оператор ORDER BYГруппировка, оператор GROUP BYАгрегатные функцииОператор HAVING"
            self.app.assertions.assertion_text(actual_text, expected_text)

    # Функция проверки наличия блока "Попрактикуйся в решении задач в удобном тренажёре" с описанием
    def check_tasks_plane(self):
        wd = self.app.wd
        locator = "//div[@class='sc-1b9df9ab-17 dOQUSG']//div[@class='sc-1b9df9ab-18 iPKjtS']"
        with allure.step('Проверка наличия заголовка блока задач'):
            title = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(title)
        with allure.step('Проверка текста заголовка блока задач'):
            actual_text = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_text = "Получи необходимые знания по SQL на нашем бесплатном курсе"
            self.app.assertions.assertion_text(actual_text, expected_text)

        locator = "//div[@class='sc-1b9df9ab-21 eyAAAE']/div[@class='sc-1b9df9ab-22 gWzNrI']"
        with allure.step('Проверка наличия описания задач'):
            title = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(title)
        with allure.step('Проверка текста заголовка блока задач'):
            actual_text = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_text = " Задачи приближены к реальным Задачи разбиты на несколько уровней сложности Весь ваш прогресс сохраняется"
            self.app.assertions.assertion_text(actual_text, expected_text)

        locator = "//div[@class='sql-editor editor-panel']"
        with allure.step('Проверка блока sql'):
            title = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(title)
        with allure.step('Проверка текста блока sql'):
            actual_text = wd.find_element(By.XPATH, f"{locator}").get_attribute("outerText")
            expected_text = "1\n2\n3\n4\n5\n-- Этот тот случай, когда редактор настолько прекрасен 😻, \n-- что лучше самому попробовать,\n-- а не просто прочитать о нем маркетинговые лозунги\nSELECT 'take a try'; "
            self.app.assertions.assertion_text(actual_text, expected_text)

    # Функция проверки наличия заголовка блока со статистикой
    def check_statistic(self):
        wd = self.app.wd
        locator = "//div[@class='sc-1b9df9ab-27 bEKsSG']//div[@class='sc-1b9df9ab-28 gFLOKs']"
        with allure.step('Проверка блока статистики пользователей'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)

    # Функция проверки наличия блока со статистикой и кнопкой Присоединиться
    def check_button_join(self):
        wd = self.app.wd
        locator = "//div[@class='sc-1b9df9ab-29 nGfyo']//button[@class='sc-14ab0bce-0 kMYtuP']"
        with allure.step('Проверка блока статистики пользователей'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка названия кнопки Присоединиться'):
            actual_text = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_text = "Присоединиться"
            self.app.assertions.assertion_text(actual_text, expected_text)

    # Функция проверки наличия ссылки на ВК
    def check_social_vk(self):
        wd = self.app.wd
        locator = "//footer[@class='footer']//div[@class='vk']/a"
        with allure.step('Проверка блока ВК'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка ссылки блока ВК'):
            actual_link = wd.find_element(By.XPATH, f"{locator}").get_attribute("href")
            expected_link = "https://vk.com/sqlacademy"
            self.app.assertions.assertion_text(actual_link, expected_link)

    # Функция проверки наличия Email для связи
    def check_social_email(self):
        wd = self.app.wd
        locator = "//footer[@class='footer']//div[@class='info'][1]/a"
        with allure.step('Проверка блока mail'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка ссылки блока mail'):
            actual_result = wd.find_element(By.XPATH, f"{locator}").get_attribute("href")
            expected_result = "mailto:admin@sql-academy.org"
            self.app.assertions.assertion_text(actual_result, expected_result)

    # Функция проверки наличия кнопки "Пользовательское соглашение"
    def check_terms_of_use(self):
        wd = self.app.wd
        locator = "//footer[@class='footer']//div[@class='info'][2]/a"
        with allure.step('Проверка блока Пользовательское соглашение'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка ссылки Пользовательское соглашение'):
            actual_result = wd.find_element(By.XPATH, f"{locator}").get_attribute("href")
            expected_result = "https://sql-academy.org/terms-of-use"
            self.app.assertions.assertion_text(actual_result, expected_result)

    # Функция проверки наличия кнопки выбора языка
    def check_button_lang(self):
        wd = self.app.wd
        locator = "//footer[@class='footer']//div[@class='lang']"
        with allure.step('Проверка блока Пользовательское соглашение'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка ссылки Пользовательское соглашение'):
            actual_result = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_result = "Русский"
            self.app.assertions.assertion_text(actual_result, expected_result)

    # Функция проверки сообщения об успешной авторизации
    def check_notification_success(self):
        wd = self.app.wd
        locator = "//div[@class='notification notification-success notification-enter-done']"
        with allure.step('Проверка наличия уведомления об успешной авторизации'):
            element = wd.find_elements(By.XPATH, f"{locator}")
            self.app.assertions.assertion_count_elements(element)
        with allure.step('Проверка текста уведомления об успешной авторизации'):
            actual_result = wd.find_element(By.XPATH, f"{locator}").get_attribute("textContent")
            expected_result = "Вы успешно авторизовались Спасибо за возвращение!"
            self.app.assertions.assertion_text(actual_result, expected_result)







