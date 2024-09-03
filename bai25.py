# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:57:45 2024

@author: ADMIN
"""

a = input("Hãy nhập một chữ cái: ")
if a.islower():
    print("Ký tự chữ hoa:", a.upper())
else:
    print("Ký tự chữ thường:", a.lower())