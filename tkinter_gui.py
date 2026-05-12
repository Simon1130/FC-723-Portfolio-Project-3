import tkinter as tk
from calculator_backend import Calculator


window = tk.Tk()
window.title("Calculator")
window.geometry("420x560")
window.resizable(False, False)

cal = Calculator()

expression = ""


# 顯示答案和輸入的地方
display = tk.Entry(window, font=("Arial", 24), justify="right", bd=8)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)


def show():
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def add_text(text):
    global expression
    expression = expression + text
    show()


def clear():
    global expression
    expression = ""
    show()


def delete():
    global expression
    expression = expression[:-1]
    show()


def answer():
    global expression

    result = cal.calculate(expression)

    display.delete(0, tk.END)
    display.insert(tk.END, result)

    if result == "Error" or result == "Cannot divide by 0":
        expression = ""
    else:
        expression = result


def change_mode():
    mode = cal.change_angle_mode()
    btn_deg.config(text=mode)


def click(value):
    if value == "C":
        clear()

    elif value == "DEL":
        delete()

    elif value == "=":
        answer()

    elif value == "sin":
        add_text("sin(")

    elif value == "cos":
        add_text("cos(")

    elif value == "tan":
        add_text("tan(")

    elif value == "√":
        add_text("sqrt(")

    elif value == "π":
        add_text("pi")

    elif value == "^":
        add_text("**")

    elif value == "DEG" or value == "RAD":
        change_mode()

    else:
        add_text(value)


# 第一行按鈕
btn_deg = tk.Button(window, text="DEG", font=("Arial", 15), width=6, height=2, command=lambda: click(btn_deg["text"]))
btn_deg.grid(row=1, column=0, padx=5, pady=5)

btn_sin = tk.Button(window, text="sin", font=("Arial", 15), width=6, height=2, command=lambda: click("sin"))
btn_sin.grid(row=1, column=1, padx=5, pady=5)

btn_cos = tk.Button(window, text="cos", font=("Arial", 15), width=6, height=2, command=lambda: click("cos"))
btn_cos.grid(row=1, column=2, padx=5, pady=5)

btn_tan = tk.Button(window, text="tan", font=("Arial", 15), width=6, height=2, command=lambda: click("tan"))
btn_tan.grid(row=1, column=3, padx=5, pady=5)


# 第二行
tk.Button(window, text="C", font=("Arial", 15), width=6, height=2, command=lambda: click("C")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text="DEL", font=("Arial", 15), width=6, height=2, command=lambda: click("DEL")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(window, text="(", font=("Arial", 15), width=6, height=2, command=lambda: click("(")).grid(row=2, column=2, padx=5, pady=5)
tk.Button(window, text=")", font=("Arial", 15), width=6, height=2, command=lambda: click(")")).grid(row=2, column=3, padx=5, pady=5)


# 第三行
tk.Button(window, text="√", font=("Arial", 15), width=6, height=2, command=lambda: click("√")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(window, text="π", font=("Arial", 15), width=6, height=2, command=lambda: click("π")).grid(row=3, column=1, padx=5, pady=5)
tk.Button(window, text="%", font=("Arial", 15), width=6, height=2, command=lambda: click("%")).grid(row=3, column=2, padx=5, pady=5)
tk.Button(window, text="/", font=("Arial", 15), width=6, height=2, command=lambda: click("/")).grid(row=3, column=3, padx=5, pady=5)


# 第四行
tk.Button(window, text="7", font=("Arial", 15), width=6, height=2, command=lambda: click("7")).grid(row=4, column=0, padx=5, pady=5)
tk.Button(window, text="8", font=("Arial", 15), width=6, height=2, command=lambda: click("8")).grid(row=4, column=1, padx=5, pady=5)
tk.Button(window, text="9", font=("Arial", 15), width=6, height=2, command=lambda: click("9")).grid(row=4, column=2, padx=5, pady=5)
tk.Button(window, text="*", font=("Arial", 15), width=6, height=2, command=lambda: click("*")).grid(row=4, column=3, padx=5, pady=5)


# 第五行
tk.Button(window, text="4", font=("Arial", 15), width=6, height=2, command=lambda: click("4")).grid(row=5, column=0, padx=5, pady=5)
tk.Button(window, text="5", font=("Arial", 15), width=6, height=2, command=lambda: click("5")).grid(row=5, column=1, padx=5, pady=5)
tk.Button(window, text="6", font=("Arial", 15), width=6, height=2, command=lambda: click("6")).grid(row=5, column=2, padx=5, pady=5)
tk.Button(window, text="-", font=("Arial", 15), width=6, height=2, command=lambda: click("-")).grid(row=5, column=3, padx=5, pady=5)


# 第六行
tk.Button(window, text="1", font=("Arial", 15), width=6, height=2, command=lambda: click("1")).grid(row=6, column=0, padx=5, pady=5)
tk.Button(window, text="2", font=("Arial", 15), width=6, height=2, command=lambda: click("2")).grid(row=6, column=1, padx=5, pady=5)
tk.Button(window, text="3", font=("Arial", 15), width=6, height=2, command=lambda: click("3")).grid(row=6, column=2, padx=5, pady=5)
tk.Button(window, text="+", font=("Arial", 15), width=6, height=2, command=lambda: click("+")).grid(row=6, column=3, padx=5, pady=5)


# 第七行
tk.Button(window, text="0", font=("Arial", 15), width=6, height=2, command=lambda: click("0")).grid(row=7, column=0, padx=5, pady=5)
tk.Button(window, text=".", font=("Arial", 15), width=6, height=2, command=lambda: click(".")).grid(row=7, column=1, padx=5, pady=5)
tk.Button(window, text="^", font=("Arial", 15), width=6, height=2, command=lambda: click("^")).grid(row=7, column=2, padx=5, pady=5)
tk.Button(window, text="=", font=("Arial", 15), width=6, height=2, command=lambda: click("=")).grid(row=7, column=3, padx=5, pady=5)


window.mainloop()