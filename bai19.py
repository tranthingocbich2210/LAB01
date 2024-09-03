# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:08:15 2024

@author: ADMIN
"""
#Nhập số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
# Tìm số nhỏ nhất
# So sánh a với b, c và d
if a <= b and a <= c and a <= d:
    so_nho_nhat = a
elif b <= a and b <= c and b <= d:
    so_nho_nhat = b
elif c <= a and c <= b and c <= d:
    so_nho_nhat = c
else:
    so_nho_nhat = d
print("Số nhỏ nhất là:", so_nho_nhat)
