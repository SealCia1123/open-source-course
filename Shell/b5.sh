#!/bin/bash
read -p "Nhap thu muc can kiem tra: " dir
if [[ ! -d $dir ]]; then
    echo "Khong tim thay"
else
    echo "Noi dung trong thu muc: "
    ls -l "$dir" | grep -v "^d"
    # find -type f
fi
