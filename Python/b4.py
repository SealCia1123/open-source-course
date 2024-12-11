#!/usr/bin/env python3
a = input("Nhap vao so thu nhat: ")
b = input("Nhap vao so thu hai: ")
c = input("Nhap vao so thu ba: ")
max = a
if max > b:
    if max < c:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
print("Max: ", max)
