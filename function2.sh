# Deklarasi Function Syntax-2
#function namaFungsi {
#   Statement-1 command...
#   Statement-2 command...
#   Statement-3 command...
#   Etc
#}

#Contoh Function Syntax-2
#!/bin/bash

#Mendeklarasikan fungsi
function nama {
    echo "Siapa namamu?"
    read nama
}
function npm {
    echo "Sebutkan NPM mu!"
    read npm
    echo -e "Hai $nama dengan NPM $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#Memanggil fungsi 
nama
npm
