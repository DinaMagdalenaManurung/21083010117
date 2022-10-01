#Syntax
#until kondisi
#do
#   perintah
#done

#Contoh
#!/bin/bash

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=$((a + 2))
done
