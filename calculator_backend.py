#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:26:32 2026

@author: simon
"""
import math 

class Calculator:
    def __init__(self):
        self.mode = "Degrees"

    def change_mod(self, mode_want_to_change):
        if mode_want_to_change in ["Degrees", "Radians"]: #input can only to be switch to these two function
            if self.mode != mode_want_to_change:
                self.mode = mode_want_to_change
    
    def addition(self, x,y):
        return x + y
        
    def subtraction(self, x,y):
        return x - y
    
    def multiplication(self, x,y):
        return x * y
    
    def division(self, x,y): # cant be divide by 0
        if y == 0:
            return "Error"
        return x / y
    
    def square(self,x): #only for power 2 square
        return x ** 2
    
    def power_square(self, x,power): #accept any input of powers
        return math.pow(x, power)
    
    def square_root(self, x): #input of sqrt can not be nagetive
        if x < 0:
            return "Error"
        return math.sqrt(x)
    
    def sin(self, x):
        if self.mode == "Degrees":
            return math.sin(math.radians(x))
        return math.sin(x)
    
    def cos(self, x):
        if self.mode == "Degrees":
            return math.cos(math.radians(x))
        return math.cos(x)
    
    def tan(self, x):
        if self.mode == "Degrees":
            return math.tan(math.radians(x))
        return math.tan(x)
    
    def inv_sin(self,x):
        if x < -1 or x > 1: #inverse sin and cos only accept range of -1 to 1
            return "Error"
        
        if self.mode == "Degrees":
            return math.degrees(math.asin(x))
        return math.asin(x)
    
    def inv_cos(self, x):
        if x < -1 or x > 1: #inverse sin and cos only accept range of -1 to 1
            return "Error"
        
        if self.mode == "Degrees":
            return math.degrees(math.acos(x))
        return math.acos(x)
    
    def inv_tan(self, x):
        if self.mode == "Degrees":
            return math.degrees(math.atan(x))
        return math.atan(x)
    
    def calculate(self, action):
        try: #use try to prevent invalid formula that crash
            result = eval(action, {"__builtins__": None}, {
                "sin": self.sin,
                "cos": self.cos,
                "tan": self.tan,
                "inv_sin": self.inv_sin,
                "inv_cos": self.inv_cos,
                "inv_tan": self.inv_tan,
                "sqrt": self.square_root
                })
            #use eval() to take string into working code
            #use __builtins__ to prevent unauthorized access
            return result
        except ZeroDivisionError: #when there is a mathematical error
            return "Error"
        except Exception: #for all other error
            return "Error"