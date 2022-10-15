#!/bin/bash

declare -a angka;

echo
echo -n " Masukkan Nama Mahasiswa : "; read nama;
echo -n " Masukkan Batas Semester : "; read sem;

jumlah=0;
ipk_mhs=0;

echo "----------------------------------------------------------"

for ((i=1; i<=sem; i++))
do
  echo -n " Masukkan nilai IPS semester $i : "; read angka[$i];
  let jumlah=$jumlah+${angka[i]};
  let ipk_mhs=$jumlah/sem;
done

echo "----------------------------------------------------------"
echo " IPS $nama = $jumlah/$sem"
echo " IPK $nama = $ipk_mhs "
