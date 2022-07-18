from PySide6.QtWidgets import QApplication

from simple_calculator.calculator_controller import CalculatorController
from simple_calculator.calculator_model import CalculatorModel
from simple_calculator.calculator_view import CalculatorView


def main():
    calculator_app = QApplication([])

    calculator_model = CalculatorModel()
    calculator_view = CalculatorView()
    calculator_controller = CalculatorController(calculator_view, calculator_model)

    calculator_view.show()

    calculator_app.exec()


if __name__ == '__main__':
    main()
