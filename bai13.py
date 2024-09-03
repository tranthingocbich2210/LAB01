# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:21:30 2024

@author: ADMIN
"""

# Nhập ngày, tháng, năm 
day = input("Nhập ngày: ")
month = input("Nhập tháng: ")
year = input("Nhập năm: ")

# Đảm bảo ngày, tháng, năm là số và không bị trống
if day.isdigit() and month.isdigit() and year.isdigit():
    day = int(day)
    month = int(month)
    year = int(year)
    
    # Xuất theo định dạng ngày/tháng/năm
    print(f"a) Ngày/tháng/năm: {day}/{month}/{year}")
    
    # Xuất theo định dạng ngày/tháng/năm (với năm 2 chữ số)
    short_year = year % 100
    print(f"b) Ngày/tháng/năm (2 chữ số năm): {day}/{month}/{short_year}")
    
    # Xuất theo định dạng năm/tháng/ngày
    print(f"c) Năm/tháng/ngày: {year}/{month}/{day}")
else:
    print("Vui lòng nhập ngày, tháng, năm hợp lệ.")

# Nhập lại ngày/tháng/năm để làm ngược lại
date_input = input("\nNhập ngày/tháng/năm (hoặc năm/tháng/ngày) để làm ngược lại: ")

# Phân tích và chuyển đổi
if '/' in date_input:
    parts = date_input.split('/')
    if len(parts) == 3:
        try:
            if len(parts[0]) == 4:  # Nếu phần đầu là năm (4 chữ số)
                # Định dạng năm/tháng/ngày
                year, month, day = parts
                year = int(year)
                month = int(month)
                day = int(day)
                print(f"Ngày/tháng/năm: {day}/{month}/{year}")
                print(f"Ngày/tháng/năm (2 chữ số năm): {day}/{month}/{year % 100}")
            else:
                # Định dạng ngày/tháng/năm
                day, month, year = parts
                day = int(day)
                month = int(month)
                year = int(year)
                print(f"Năm/tháng/ngày: {year}/{month}/{day}")
                print(f"Ngày/tháng/năm (2 chữ số năm): {day}/{month}/{year % 100}")
        except ValueError:
            print("Định dạng ngày/tháng/năm không hợp lệ.")
    else:
        print("Định dạng nhập không đúng.")
else:
    print("Vui lòng nhập đúng định dạng ngày/tháng/năm hoặc năm/tháng/ngày.")
