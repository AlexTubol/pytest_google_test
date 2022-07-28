import pytest

from PageObject.models.calculator import GoogleCalculator
from PageObject.models.main_page import MainPage


class TestGoogleCalculator:
    @pytest.mark.calculator
    @pytest.mark.parametrize("expression, result",
                             [("1 + 2 =", "3"),
                              ("1 - 3 =", "-2"),
                              ("1 * 1 =", "1")])
    def test_google_calculator(self, driver, expression, result):
        main_page = MainPage(driver)
        main_page.go_page()

        main_page.search("Калькулятор")
        main_page.search_button()

        calculator = GoogleCalculator(driver)
        calculator.result().send_keys(expression)

        calculator.check_calculator_result(result)
