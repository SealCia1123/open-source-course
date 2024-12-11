#!/usr/bin/env python3
n = int(input("Nhap vao n: "))
sum = 0
for i in range(1, n + 1):
    num = int(input(f"Nhap vao so thu {i}: "))
    while num < 100 or num > 999:
        print("Khong duoc nhap so nam ngoai khoang 100-999")
        num = int(input(f"Nhap vao so thu {i}: "))
    sum += num
print("Tong: ", sum)
