import json
import os.path

#import jsonpickle
import pytest
#import allure
from fixture.application import Application
#import importlib
import os.path

fixture = None
target = None


# Функция чтения данных из файла target.json
def load_config(file):

    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    global browser
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
        #запуск браузера (по умолчанию chrome)
        fixture = Application(browser=browser, base_url=web_config['base_url'])
    return fixture


# Функция остановки фикстуры
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")

