#!/bin/bash
echo "Nhap ten file/duong dan can tim: "
read file_name
if [[ -e $file_name ]]; then
    echo "Tim thay file tai $(realpath $file_name)"
else
    echo "Khong tim thay file"
fi
