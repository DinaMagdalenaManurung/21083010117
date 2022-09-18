echo "Masukkan angka pertama : "
read x
echo "Masukkan angka kedua : "
read y

echo "Pilihlah operasi yang anda inginkan :"
echo "1. Penjumlahan"
echo "2. Pengurangan"
echo "3. Perkalian"
echo "4. Pembagian"
echo "Masukkan nomor operasi yang anda inginkan (1/2/3/4) :"
read operasi

if [ $operasi -eq 1 ]
then
	let hasil=x+y
	echo "Hasil penjumlahan $x dan $y ($x + $y) = $hasil"
elif [ $operasi -eq 2 ]
then
	let hasil=x-y
	echo "Hasil pengurangan $x dan $y ($x - $y) = $hasil"
elif [ $operasi -eq 3 ]
then
	let hasil=x*y
	echo "Hasil perkalian $x dan $y ($x * $y) = $hasil"
elif [ $operasi -eq 4 ]
then
	let hasil=x/y
	echo "Hasil pembagian $x dan $y ($x / $y) = $hasil"
else 
	echo "Maaf pilihan anda tidak bisa dideteksi"
fi

