# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:43:55 2024

@author: ADMIN
"""
hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))
thoi_gian = input('Nhập vào giờ, phút, giây có định dạng {} : {} : {}'.format(hh, mm, ss))
tong_giay = hh * 3600 + mm * 60 + ss
print("Tổng giây là: ", tong_giay)
