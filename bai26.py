# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:57:55 2024

@author: ADMIN
"""

# Câu a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần: ", a, b, c)
# Câu b
N = input("Nhập 1 số nguyên: ")
day_so = "".join(sorted(N))
print("Dãy số theo thứ tự tăng dần: ", day_so)