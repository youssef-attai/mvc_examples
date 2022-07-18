from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel, QPushButton


class CalculatorView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayout(QHBoxLayout(self))

        self.num1_lineedit = QLineEdit(self)
        self.num2_lineedit = QLineEdit(self)
        self.calculate_button = QPushButton("Calculate", self)
        self.result_label = QLabel(self)

        self.layout().addWidget(self.num1_lineedit)
        self.layout().addWidget(self.num2_lineedit)
        self.layout().addWidget(self.calculate_button)
        self.layout().addWidget(self.result_label)

