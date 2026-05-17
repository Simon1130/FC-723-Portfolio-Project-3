import tkinter as tk
import math
from calculator_backend import Calculator 

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calc = Calculator()
        self.expression = ""
        
        #layout design
        self.display = tk.Entry(root, font = ("Arial", 30), justify = "right", bd=15, bg = "grey", relief = "ridge") 
        self.display.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)
        
        #all buttons list 
        buttons = [
            'sin', 'cos', 'tan', 'x²', 'x^p',
            'inv_sin', 'inv_cos', 'inv_tan', 'sqrt', 'π',
            '7', '8', '9','DEL','AC',
            '4', '5', '6', '*', '÷',
            '1', '2', '3', '+', '-',
            '0', '.', '(', ')', '=',
            'Mode'
        ]

        row, column = 1, 0 #as counts
        for button in buttons:
            #
            tk.Button(root, text=button, width=7, height=4, 
            #lambda is use to store the button text to the display when button has clicked
                      command = lambda text = button: self.run_input(text)).grid(row = row, column = column, padx = 2, pady = 2)
            column += 1
            if column > 4: 
                column = 0
                row += 1
        
        
    def run_input(self, input_action):
        current_display = self.display.get()
        
        if current_display == "Error": #auto delete when there are 'Error' in display
            self.display.delete(0, tk.END)
            current_display = ""
            
        if input_action == '=':
            result = self.calc.calculate(current_display) 
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            
        elif input_action == 'Mode': #switch mode to another one if button is click
            new_mode = "Radians" if self.calc.mode == "Degrees" else "Degrees"
                
            self.calc.change_mod(new_mode)
            # Update the window title of the mode
            self.root.title(f"Scientific Calculator - {new_mode.upper()}")
        
        elif input_action == 'AC': #All Clear
            if self.display:
                self.display.delete(0, tk.END)
            
        elif input_action == 'DEL': #Delete one symbol only
            self.display.delete(len(current_display) - 1, tk.END)
        
        elif input_action == "÷": #use divison simbol
            self.display.insert(tk.END, "/")
        elif input_action == "x²":
            self.display.insert(tk.END, "**2")
        elif input_action == "x^p":
            self.display.insert(tk.END, "**")
        elif input_action == "π":
            self.display.insert(tk.END, str(math.pi))
        elif input_action in ['sin', 'cos', 'tan', 'inv_sin', 'inv_cos', 'inv_tan', 'sqrt']:
            self.display.insert(tk.END, input_action + '(') #automates add square bracket for easier use
        
        else:
            
            self.display.insert(tk.END, input_action)

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
    