from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url, *args, **kwargs):
        super().__init__(browser, url)

#метод __init__ вызывается при создании объекта.
# Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы,
# которые мы передали в конструктор MainPage