# Syntax
#while kondisi
#do
#   perintah
#done

#Contoh
#!/bin/bash
a=0

while [ $a -lt 10 ]
do
   echo $a
   a=$((a+2))
done
