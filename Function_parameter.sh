#Bash Function dengan Parameter (x,y)

#Deklarasi function parameter
#function namaFungsi atau namaFungsi() {
#  par1=$1
#  par2=$2
#  command on $par1
#}

#Contoh function parameter
#!/bin/bash

#Mendeklarasikan fungsi
identitas() {
        parameter1=$1
        parameter2=$2
        parameter3=$3
        echo "$parameter1"
        echo "$parameter2"
        echo "$parameter3"
}

echo "Masukkan Nama : "
read a
echo "Masukkan NPM : "
read b
echo "Hobimu apa? : "
read c

printf "\n"
identitas $a $b $c
