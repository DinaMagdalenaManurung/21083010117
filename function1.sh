# Deklarasi Function Syntax-1
#nama_fungsi () {
#    perintah1
#    perintah2
#    ...
#    perintahLain
#}

#Contoh function syntax-1
#!/bin/bash

#Mendeklarasikan fungsi
nama() {
    echo "Siapa namamu?"
    read nama
}
npm() {
   echo "Sebutkan npm mu"
   read npm
   echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#Memanggil fungsi
nama
npm
