#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:43:53 2026

@author: simon
"""
import unittest
from unittest import TestCase
from calculator_backend import Calculater

class TestCal(TestCase):
    def setUp(self):
        self.cal = Calculater()
    
    def test_divide_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            self.cal.division(10, 0)
            
    def test_negative_sqrt(self):
        with self.assertRaises(ValueError):
            self.cal.square_root(-1)
            
    def test_inv_sin_input_morethan_1(self):
        with self.assertRaises(ValueError):
            self.cal.inv_sin(2)

if __name__ == '__main__':
    unittest.main()
