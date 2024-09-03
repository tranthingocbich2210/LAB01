# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:57:41 2024

@author: ADMIN
"""

# Giờ đầu tiên
a = int(input("Nhập giờ (1): "))
b = int(input("Nhập phút (1): "))
c = int(input("Nhập giây (1): "))
d = a*3600+b*60+c
print("Thời gian (1):",f"{a}h{b}p{c}s","=",d,"giây")
# Giờ thứ hai
x = int(input("Nhập giờ (2): "))
y = int(input("Nhập phút (2): "))
z = int(input("Nhập giây (2): "))
t = x*3600+y*60+z
print("Thời gian (2):",f"{x}h{y}p{z}s","=",t,"giây")
# In ra kết quả
print("Thời gian (1) + Thời gian (2) = ",d+t)
print("Thời gian (1) - Thời gian (2) = ",d-t)
print("Thời gian (2) - Thời gian (1) = ",t-d)