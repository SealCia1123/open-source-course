#!/usr/bin/env python3
n = int(input("Nhap vao n: "))
sum = 0
nums = []
for i in range(1, n + 1):
    num = int(input(f"Nhap vao so thu {i}: "))
    if num % 2 == 0:
        nums.append(num)

print("Cac so chan la: ", end="")
for i in nums:
    print(f"{i} ", end="")
