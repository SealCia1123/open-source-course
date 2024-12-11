#!/bin/bash
read -p "Nhap file/duong dan den file muon doc: " file
if [[ -f $file ]]; then
    echo "Noi dung file:"
    cat "$file"
else
    echo "Khong tim thay file"
fi
