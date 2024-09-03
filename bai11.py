# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:01:40 2024

@author: ADMIN
"""
# Nhập ký tự chữ thường từ người dùng
char_lower = input("Nhập một ký tự chữ thường: ")

# Kiểm tra xem đầu vào có phải là một ký tự chữ thường không
if len(char_lower) == 1 and char_lower.islower():
    # Chuyển ký tự chữ thường thành chữ hoa
    char_upper = char_lower.upper()
    print("Ký tự chữ hoa tương ứng là", char_upper)
else:
    print("Vui lòng nhập một ký tự chữ thường hợp lệ.")



 
 
 
    