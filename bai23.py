# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:55:39 2024

@author: ADMIN
"""

import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
# Tính
delta=float()
delta = (b**2) - (4*a*c)
if a == 0:
    print("Phương trình không phải phương trình bậc 2")
elif delta > 0:
    x1 = -b + math.sqrt(delta) / 2*a
    x2 = -b - math.sqrt(delta) / 2*a
    print("Phương trình có 2 nghiệm là: ",x1, x2)
elif delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 =", -b/2*a)