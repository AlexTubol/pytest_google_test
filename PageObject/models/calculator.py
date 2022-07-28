"""Калькулятор"""


class GoogleCalculator:
    CalculatorResult = '//div[@class = "card-section"]//div[@role="presentation"]'

    def __init__(self, driver):
        self.driver = driver

    def result(self):
        return self.driver.find_element_by_xpath(GoogleCalculator.CalculatorResult)

    def check_calculator_result(self, result):
        field = self.result()
        assert field.text == result
