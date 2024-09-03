# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:19:17 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên dương a:"))
b = int(input("Nhập số nguyên dương b:"))
# Điều kiện a và b đều phải 
if a > 0 and b > 0:
    # Tính chia phần nguyên và phần 
    thuong_lay_nguyen = a//b
    thuong_lay_du = a % b 
    # In kết quả
    print("Kết quả chia lấy phần nguyên của a và b", thuong_lay_nguyen)
    print("Kết quả chia lấy phần dư của a và b", thuong_lay_du)
else:
    print("Số nhập vào không phải là số nguyên dương.")  