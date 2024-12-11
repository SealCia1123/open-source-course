#!/bin/bash
let sum=0
for ((i = 0; i < 100; i++)); do
    sum+=$i
done
echo "Sum $sum"
