# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:57:07 2024

@author: ADMIN
"""

s = a = 0
n = int(input("Nhập biển số xe:"))
while (n!=0):
    a = n % 10
    s = s + a
    n = n // 10
print("Số nút là:", s%10)
    
    