#!/bin/bash
printf "masukan angka : "
a=0
read input

until [ ! $input -gt $a ]
do
  echo $input
  input=$((input - 2))
done
