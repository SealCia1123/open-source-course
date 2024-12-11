#!/bin/bash
read -p "Nhap file/thu muc can kiem tra: " path
if [[ -f $path || -d $path ]]; then
    if [[ -x $path ]]; then
        echo "File/thu muc co quyen excute"
    else
        chmod +x "$path"
        echo "Da cap quyen cho $path"
    fi
else
    echo "Khong tim thay file/thu muc da chi dinh"
fi
