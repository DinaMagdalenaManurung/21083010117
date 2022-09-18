#!/bin/bash

# membuat variabel tidak boleh ada spasi antar variabel dan simbol "="
a=15 # membuat variabel a = 15
b=7 # membuat variabel b = 7

# memakai let
# memanggil variabel diatas menggunakan $
# Format : let variabel_rumus=$a+$b (+ sesuai oprasi math yg digunakan)
let jumlah=$a+$b # membuat perintah let dengan rumus jumlah
let "kurang = $a-$b" # mencoba dengan tanda petik
let kali=$a*$b

# memakai expr
# mengunakan petik `~`
bagi=`expr $a / $b`

# memakai perintah subsitusi $((ekspresi))
mod=$(($a % $b))

echo "a + b = $jumlah"
echo "a - b = $kurang"
echo "a * b = $kali"
echo "a % b = $mod"

# variabel b diubah menjadi sama dengan hasil variabel a yaitu 15
b=$a

echo "a = $a"
echo "b = $b"
