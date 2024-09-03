# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:57:26 2024

@author: ADMIN
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
# Biểu thức
A = ((a+b)/(pow(a,1/3)+pow(b,1/3))-pow(a*b,1/3))/(pow(a,1/3)-pow(b,1/3))**2
print("Kết quả biểu thức là: ", A)