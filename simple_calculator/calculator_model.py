class CalculatorModel:
    def __init__(self):
        self.__calculation_value = 0

    def add_two_numbers(self, num1, num2):
        self.__calculation_value = num1 + num2

    def get_calculation_value(self):
        return self.__calculation_value
