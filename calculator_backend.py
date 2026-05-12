#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:26:32 2026

@author: simon
"""
import math 

class Calculater:
    
    def addition(x,y):
        return x + y
        
    def subtraction(x,y):
        return x - y
    
    def multiplication(x,y):
        return x * y
    
    def Division(x,y):
        return x / y
    
    def square(x,index):
        return math.pow(x, index)
    
    def square_root(x):
        return math.sqrt(x)
    
    def sin(x):
        return math.sin(math.radians(x))
    
    def cos(x):
        return math.cos(math.radians(x))
    
    def tan(x):
        return math.tan(math.radians(x))
    
    def inv_sin(x):
        return math.degrees(math.asin(x))
    
    def inv_cos(x):
        return math.degrees(math.acos(x))
    
    def inv_tan(x):
        return math.degrees(math.atan(x))