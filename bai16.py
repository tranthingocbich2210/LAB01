# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:12:51 2024

@author: ADMIN
"""
gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))

# Tính tổng đổi ra giây
tong_giay = gio*3600 + phut*60 + giay
print("Tổng đổi ra giây:", tong_giay)