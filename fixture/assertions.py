
class AssertionsHelper:
    def __init__(self, app):
        self.app = app

    # Функция проверки, что на странице найден 1 элемент
    def assertion_count_elements(self, element):
        assert len(element) == 1, "Элемент не найден"

    # Функция проверки текста (текст страницы = текст ожидаемый)
    def assertion_text(self, actual_text, expected_text):
        assert actual_text == expected_text, f"Текст на странице {actual_text} не совпадает с ожидаемым {expected_text}"