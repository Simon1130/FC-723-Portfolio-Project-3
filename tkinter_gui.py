import tkinter as tk

from calculator_backend import Calculator 

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calc = Calculator()
        self.expression = ""
        
        
        self.display = tk.Entry(root, font=("Arial", 24), justify="right", bd=9)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        #row 1 buttons
        btn7 = tk.Button(root, text="7", width=5, height=2, command=lambda: self.on_click("7"))
        btn7.grid(row=1, column=0)
        
        btn8 = tk.Button(root, text="8", width=5, height=2, command=lambda: self.on_click("8"))
        btn8.grid(row=1, column=1)
        
        btn9 = tk.Button(root, text="9", width=5, height=2, command=lambda: self.on_click("9"))
        btn9.grid(row=1, column=2)
        
        btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda: self.on_click("/"))
        btn_div.grid(row=1, column=3)

    def on_click(self, char):
        if char == '=':
            
            try:
                
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
