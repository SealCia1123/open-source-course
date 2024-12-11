#!/usr/bin/env python3
str = input("Nhap vao chuoi: ")
count_alpha = 0
count_digit = 0
for i in str:
    if i.isalpha():
        count_alpha += 1
    elif i.isdigit():
        count_digit += 1
print("So chu cai:", count_alpha)
print("So chu so:", count_digit)
