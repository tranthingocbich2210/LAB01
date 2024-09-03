# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:10:35 2024

@author: ADMIN
"""

# Nhập ba số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

# Tìm số lớn nhất
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c

print("Số lớn nhất là:", so_lon_nhat)
