# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:15:34 2024

@author: ADMIN
"""

a = int(input("Nhập 1 số bất kì: "))
list = ["khong", "mot", "hai", "ba", "tu", "nam", "sau", "bay", "tam", "chin"]
if 0<=a<=9:
    print(list[a])
else:
    print("Khong doc duoc")