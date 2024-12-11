#!/usr/bin/env python3

chuoi1 = (
    "Tri tue nhan tao ngay nay co the thay the con "
    "nguoi lam mot so cong viec nhat dinh"
)
chuoi2 = "con nguoi ngay nay"
words = chuoi2.split(" ")
result = chuoi1
for i in words:
    result = result.replace(i, "")
result = " ".join(result.split())
writer = open("ketqua.txt", "w")
writer.write(result)
print("Ghi file thanh cong!")
