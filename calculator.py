import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #333333;")

        # Set central widget and layout
        widget = QWidget(self)
        self.setCentralWidget(widget)
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)

        # Display field
        self.display = QLineEdit()
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            "font-size: 24px; color: white; background-color: #2c2c2c; border: none; padding: 10px;"
        )
        self.layout.addWidget(self.display)

        # Grid layout for buttons
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Button labels and functions
        buttons = [
            ['sin', 'cos', 'tan', 'log', 'sqrt'],
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', 'x!'],
            ['1', '2', '3', '-', '1/x'],
            ['0', '=', '+', '^2', '10^x']
        ]

        # Map the button labels to functions
        self.ops = {
            'sin': lambda: self.perform_trig_function(math.sin),
            'cos': lambda: self.perform_trig_function(math.cos),
            'tan': lambda: self.perform_trig_function(math.tan),
            'log': self.logarithm,
            'sqrt': self.square_root,
            'x!': self.factorial,
            '1/x': self.reciprocal,
            '^2': self.square,
            '10^x': self.power_of_ten,
        }

        # Create buttons in grid layout
        self.create_buttons(buttons)

    def create_buttons(self, buttons):
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                button = QPushButton(label)
                button.setFixedSize(70, 70)  # Smaller button size
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #e0e0e0;
                        border-radius: 15px;
                        font-size: 18px;
                        color: #333;
                        border: none;
                    }
                    QPushButton:pressed {
                        background-color: #cccccc;
                    }
                """)
                if label in self.ops:
                    button.clicked.connect(self.ops[label])
                else:
                    button.clicked.connect(partial(self.on_button_click, label))
                self.grid_layout.addWidget(button, i, j)

    def on_button_click(self, label):
        if label == '=':
            self.calculate_expression()
        elif label == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + label)

    def calculate_expression(self):
        try:
            result = eval(self.display.text())
            self.display.setText(f"{result:.6g}")
        except Exception:
            self.display.setText("Error")

    def perform_trig_function(self, func):
        try:
            result = func(math.radians(float(self.display.text())))
            self.display.setText(f"{result:.6f}")
        except Exception:
            self.display.setText("Error")

    def square(self):
        try:
            result = float(self.display.text()) ** 2
            self.display.setText(f"{result:.6g}")
        except Exception:
            self.display.setText("Error")

    def logarithm(self):
        try:
            value = float(self.display.text())
            if value <= 0:
                raise ValueError
            result = math.log(value)
            self.display.setText(f"{result:.6f}")
        except Exception:
            self.display.setText("Error")

    def reciprocal(self):
        try:
            result = 1 / float(self.display.text())
            self.display.setText(f"{result:.6f}")
        except Exception:
            self.display.setText("Error")

    def factorial(self):
        try:
            result = math.factorial(int(self.display.text()))
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")

    def power_of_ten(self):
        try:
            result = 10 ** float(self.display.text())
            self.display.setText(f"{result:.6g}")
        except Exception:
            self.display.setText("Error")

    def square_root(self):
        try:
            result = math.sqrt(float(self.display.text()))
            self.display.setText(f"{result:.6g}")
        except Exception:
            self.display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
