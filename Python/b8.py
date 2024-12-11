#!/usr/bin/env python3
arr = [23, 76, 12, 1, 97, 26, 31]
sum = 0
for i in range(len(arr)):
    if i % 2 == 0:
        sum += arr[i]
print("Tong cac phan tu o vi tri chan: ", sum)
