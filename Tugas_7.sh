#Membuat program bash function yang dapat menghitung luas bidang persegi panjang
#Menggunakan Bash Function dengan Parameter (x,y)

#!/bin/bash

echo ">>Menghitung luas persegi panjang<<";
echo

L_PersegiPanjang() {
  panjang=$p
  lebar=$l
  echo "$panjang"
  echo "$lebar"
}

echo "Masukkan Panjang (cm)  :"
read panjang;
echo "Masukkan Lebar (cm)  :"
read lebar;
let hasil=$panjang*$lebar
echo "Jadi, Luas persegi panjang adalah $hasil cm^2 "

printf "\n"
L_PersegiPanjang $panjang $lebar
