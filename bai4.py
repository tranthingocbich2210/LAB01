# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:35:53 2024

@author: ADMIN
"""

# Nhập số nguyên dương có 2 chữ số
N = int(input("Nhập số nguyên dương có 2 chữ số:"))
#Kiểm tra số nhập có đủ 2 số không
if 1<= N <= 99:
    #Tách các chữ số
    #Chữ số hàng chục
    chuc = N // 10
    #Chữ số hàng đơn vị
    don_vi = N % 10
    #Tính tổng các chữ số
    tong = chuc + don_vi
else:
    print("Số nhập vào không phải là số nguyên dương có 2 số")
# In ra kết quả
print("Kết quả", chuc + don_vi)