# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:09:41 2024

@author: ADMIN
"""
# Nhập ba số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

# Tìm số lớn nhất
so_lon_nhat = max(a, b, c)

# Tìm số nhỏ nhất
so_nho_nhat = min(a, b, c)

print("Số lớn nhất là:", so_lon_nhat)
print("Số nhỏ nhất là:", so_nho_nhat)
