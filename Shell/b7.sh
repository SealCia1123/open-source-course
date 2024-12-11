#!/bin/bash
read -p "Nhap thu muc can xoa: " dir
read -p "Nhap phan extension can xoa: " ex

if [[ -d $dir ]]; then
    rm "$dir"/*."$ex"
else
    echo "Khong tim thay thu muc"
fi
