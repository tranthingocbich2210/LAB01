# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:28:10 2024

@author: ADMIN
"""
# Nhập cân nặng và chiều cao
a = float(input("Nhập cân nặng của bạn(kg):"))
b = float(input("Nhập chiều cao của bạn(m):"))
# Tính BMI
bmi = a / (b ** 2)
# In kết quả
print("Kết quả BMI của bạn là:", bmi)
# Phân loại chỉ số BMI
if bmi < 18.5:
    print("Bạn bị gầy.")
elif 18.5 <= bmi < 24.9:
    print("Bạn có cân nặng bình thường.")
elif 25 <= bmi < 29.9:
    print("Bạn bị thừa cân.")
else:
    print("Bạn bị béo phì.")
