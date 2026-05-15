import tkinter as tk
import math
from calculator_backend import Calculator


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calc = Calculator()
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 24), justify="right", bd=9)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            'sin', 'cos', 'tan', 'inv_sin', 'inv_cos',
            'inv_tan', 'sqrt', 'x²', 'x^p', '(',
            ')', 'π', '7', '8', '9',
            '÷', '4', '5', '6', '*',
            'C', '1', '2', '3', '-',
            'Mode', '0', '.', '=', '+',
            'DEL'
        ]

        row, column = 1, 0
        for button in buttons:
            #
            tk.Button(root, text=button, width=8, height=2,
                      command=lambda text=button: self.run_input(text)).grid(row=row, column=column, padx=2, pady=2)
            column += 1
            if column > 4:
                column = 0
                row += 1

    def run_input(self, input_action):
        current_display = self.display.get()

        if input_action == '=':
            result = self.calc.calculate(current_display)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))

        elif input_action == 'Mode':
            if self.calc.mode == "Degrees":
                new_mode = "Radians"
            else:
                new_mode = "Degrees"

            self.calc.change_mod(new_mode)
            # Update the window title of the mode
            self.root.title(f"Scientific Calculator - {new_mode.upper()}")

        elif input_action == 'C':
            if self.display:
                self.display.delete(0, tk.END)

        elif input_action == 'DEL':
            self.display.delete(len(current_display) - 1, tk.END)

        elif input_action == "÷":
            self.display.insert(tk.END, "/")
        elif input_action == "x²":
            self.display.insert(tk.END, "**2")
        elif input_action == "x^p":
            self.display.insert(tk.END, "**")
        elif input_action == "π":
            self.display.insert(tk.END, str(math.pi))
        else:

             self.display.insert(tk.END, input_action)


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()