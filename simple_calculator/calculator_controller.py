from simple_calculator.calculator_model import CalculatorModel
from simple_calculator.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self, view: CalculatorView, model: CalculatorModel):
        self.model = model
        self.view = view

        self.view.calculate_button.pressed.connect(self.calculate)

    def calculate(self):
        try:
            self.model.add_two_numbers(int(self.view.num1_lineedit.text()), int(self.view.num2_lineedit.text()))
            self.view.result_label.setText(str(self.model.get_calculation_value()))
        except ValueError:
            self.view.result_label.setText("Please enter valid numbers")
