#!/bin/bash
start_value=10
read -p "Nhap ten file muon tao: " name
read -p "Nhap so luong file can tao: " number
let n=number+10
# for i in $(seq $start_value $n); do
for ((i = 10; i < $n; i++)); do
    touch $name$i.txt
done
