"""Главная страница."""


class MainPage:
    SearchBox = "q"
    SearchButton = "btnK"

    def __init__(self, driver):
        self.url = "https://google.com"
        self.driver = driver

    def go_page(self):
        return self.driver.get(self.url)

    def search(self, text):
        search_box = self.driver.find_element_by_name(MainPage.SearchBox)
        search_box.send_keys(text)

    def search_button(self):
        return self.driver.find_element_by_name(MainPage.SearchButton).click()
