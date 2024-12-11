#!/bin/bash

read -p "Nhap ten file/duong dan can tim: " file_name
while [[ $file_name != *.* ]]; do
    echo "File can tim phai la file va co phan mo rong"
    read -p "Vui long nhap lai: " file_name
done

if find ~ -type f -name $file_name &>/dev/null; then
    echo "Found"
else
    echo "Not found"
fi
