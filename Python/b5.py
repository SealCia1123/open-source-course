#!/usr/bin/env python3
n = int(input("Nhap vao so luong can kiem tra: "))
max = int(input("Nhap vao so thu 1: "))

for i in range(1, n):
    num = int(input(f"Nhap vao so thu {i}: "))
    if max < num:
        max = num
print("Max: ", max)
