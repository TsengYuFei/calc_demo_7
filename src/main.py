import flet as ft
import math  # 引入數學庫
from calculate import Calculator
from buttons import DigitButton, OperatorButton, ActionButton

class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.expand = 1
        self.clac = Calculator()
        self.calculate = self.clac.calculate
        self.content = self.ui()

    def ui(self):
        ui = ft.Column(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[self.result],
                    alignment="end"),
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="AC",
                            button_clicked=self.button_clicked,
                            action="clear",
                        ),
                        ActionButton(
                            text="+/-",
                            button_clicked=self.button_clicked,
                            action="negate",
                        ),
                        ActionButton(
                            text="%",
                            button_clicked=self.button_clicked,
                            action="percent",
                        ),
                        OperatorButton(
                            text="÷",
                            button_clicked=self.button_clicked,
                            operations="div",
                        ),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="7", button_clicked=self.button_clicked, value=7),
                        DigitButton(
                            text="8", button_clicked=self.button_clicked, value=8),
                        DigitButton(
                            text="9", button_clicked=self.button_clicked, value=9),
                        OperatorButton(
                            text="*", button_clicked=self.button_clicked, operations="mul"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="4", button_clicked=self.button_clicked, value=4),
                        DigitButton(
                            text="5", button_clicked=self.button_clicked, value=5),
                        DigitButton(
                            text="6", button_clicked=self.button_clicked, value=6),
                        OperatorButton(
                            text="-", button_clicked=self.button_clicked, operations="sub"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="1", button_clicked=self.button_clicked, value=1),
                        DigitButton(
                            text="2", button_clicked=self.button_clicked, value=2),
                        DigitButton(
                            text="3", button_clicked=self.button_clicked, value=3),
                        OperatorButton(
                            text="+", button_clicked=self.button_clicked, operations="add"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="0", expand=1, button_clicked=self.button_clicked, value=0
                        ),
                        DigitButton(
                            text=".", button_clicked=self.button_clicked, value="."),
                        ActionButton(
                            text="⌫", button_clicked=self.button_clicked, action="backspace"),
                        ActionButton(
                            text="=", button_clicked=self.button_clicked, action="calculate"),
                    ]
                ),
                # 新增的數學操作行
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="1/x", button_clicked=self.button_clicked, action="reciprocal"),
                        ActionButton(
                            text="sin", button_clicked=self.button_clicked, action="sin"),
                        ActionButton(
                            text="cos", button_clicked=self.button_clicked, action="cos"),
                        ActionButton(
                            text="tan", button_clicked=self.button_clicked, action="tan"),
                    ]
                ),
                # 新增的平方、立方、平方根行
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="x²", button_clicked=self.button_clicked, action="square"),
                        ActionButton(
                            text="x³", button_clicked=self.button_clicked, action="cube"),
                        ActionButton(
                            text="√x", button_clicked=self.button_clicked, action="sqrt"),
                    ]
                ),
            ]
        )
        return ui

    def button_clicked(self, e):
        types = e.control.type
        if types == "digit":
            self.digit_button_clicked(e)
        elif types == "operator":
            self.operator_button_clicked(e)
        elif types == "action":
            self.action_button_clicked(e)
        else:
            raise ValueError("Invalid button type")
        self.update()

    def digit_button_clicked(self, e):
        value = e.control.value
        if self.result.value == "0" or self.new_operand == True:
            self.result.value = str(value)
            self.new_operand = False
        else:
            self.result.value = self.result.value + str(value)

    def operator_button_clicked(self, e):
        self.operator = e.control.operations
        if self.operand1 != 0:
            self.result.value = self.format_number(
                self.calculate(
                    self.operand1, float(self.result.value), self.operator
                )
            )
        if self.result.value == "Error":
            self.operand1 = "0"
        else:
            self.operand1 = float(self.result.value)
        self.new_operand = True

    def action_button_clicked(self, e):
        action = e.control.action
        if action == "clear":
            self.result.value = "0"
            self.reset()
        elif action == "negate":
            self.result.value = str(
                self.format_number(
                    -1 * float(self.result.value)
                )
            )
        elif action == "percent":
            self.result.value = str(
                self.format_number(
                    float(self.result.value) / 100
                )
            )
            self.reset()
        elif action == "calculate":
            self.result.value = self.format_number(
                self.calculate(
                    self.operand1, float(self.result.value), self.operator
                )
            )
            self.reset()
        elif action == "reciprocal":
            self.result.value = str(
                self.format_number(
                    1 / float(self.result.value)
                )
            )
        elif action == "sin":
            self.result.value = str(
                self.format_number(
                    math.sin(math.radians(float(self.result.value)))
                )
            )
        elif action == "cos":
            self.result.value = str(
                self.format_number(
                    math.cos(math.radians(float(self.result.value)))
                )
            )
        elif action == "tan":
            self.result.value = str(
                self.format_number(
                    math.tan(math.radians(float(self.result.value)))
                )
            )
        elif action == "square":
            self.result.value = str(
                self.format_number(
                    float(self.result.value) ** 2
                )
            )
        elif action == "cube":
            self.result.value = str(
                self.format_number(
                    float(self.result.value) ** 3
                )
            )
        elif action == "sqrt":
            if float(self.result.value) < 0:
                self.result.value = "Error"  # 防止根號負數
            else:
                self.result.value = str(
                    self.format_number(
                        math.sqrt(float(self.result.value))
                    )
                )
        else:
            raise ValueError("Invalid action")

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

def main(page: ft.Page):
    page.title = "Calc App"
    page.bgcolor = "#6C6C6C"
    page.window.min_width = 500
    page.window.min_height = 350
    calc = CalculatorApp()
    page.add(calc)

ft.app(target=main)
