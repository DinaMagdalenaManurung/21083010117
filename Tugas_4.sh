#!/bin/bash

echo "Masukkan bilangan acuan : "
x=0
read bilangan

until [ ! $bilangan -gt $x ]
do
   echo $bilangan
   bilangan=$((bilangan - 2))
done
