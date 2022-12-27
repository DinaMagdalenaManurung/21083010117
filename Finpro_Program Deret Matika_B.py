import os
import sys

def clear_screen():
    os.system('clear' if(os.name=='nt') else 'clear')

def penutup():
    print("\n")
    print("-"*60)
    print("-"*19, "SEMOGA MUDAH DIPAHAMI!", "-"*19)

def tanya():
    print("\n")
    input("Tekan tombol apa saja untuk kembali ke menu awal : ")
    clear_screen()
        
def menu_keluar():
    print("\n","-"*60)
    print("-"*19, "SEMOGA MUDAH DIPAHAMI!", "-"*19)
    print("-"*60)
    print("-"*14, "Terima kasih Telah Berkunjung :)", "-"*14)
    
def menu_awal():
    while(True):
        print("="*60)
        print("-"*7, "Selamat Datang di Program Deret Matematika", "-"*7)
        print("="*60)
        print("\nDaftar pilihan deret bilangan : ")
        print(" 1. Deret Aritmatika ")
        print(" 2. Deret Fibonacci")
        print(" 3. Deret Bilangan Prima")
        print(" 4. Deret Bilangan Kelipatan ")
        print(" 5. Keluar ")
        try:
            a=int(input("\nSilahkan pilih menu deret (1/2/3/4/5): "))
            print()
            if(a==1):
                print("\n","="*17, "PROGRAM DERET MATEMATIKA", "="*17)
                print("|                DERET BILANGAN ARITMATIKA                 |")
                print("="*60)
                print(deret_aritmatika())
                penutup()
                tanya()
            elif(a==2):
                print("\n","="*17, "PROGRAM DERET MATEMATIKA", "="*17)
                print("|                DERET BILANGAN FIBONACCI                   |")
                print("="*60)
                panjang = int(input('Masukkan panjang deret:'))
                print(fibonacci(panjang - 1))
                penutup()
                tanya()
            elif(a==3):
                print("\n","="*17, "PROGRAM DERET MATEMATIKA", "="*17)
                print("|                  DERET BILANGAN PRIMA                    |")
                print("="*60)
                awal = int(input("Masukkan batas awal : "))
                akhir = int(input("Masukkan batas akhir : "))
                print(cari_bilangan_prima (awal, akhir))
                penutup()
                tanya()
            elif(a==4):
                print("\n","="*17, "PROGRAM DERET MATEMATIKA", "="*17)
                print("|                 DERET BILANGAN KELIPATAN                   |")
                print("="*60)
                print(deret_kelipatan())
                penutup()
                tanya()
            elif(a==5):
                menu_keluar()
                break
            else:
                print("Masukkan angka 1-5 dengan benar!")
                menu_awal()
                continue
        except ValueError:
            print("Masukkan sesuai yang ada di daftar menu!")
            menu_awal()
            continue
            
def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True
def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima
    
def fibonacci (n):
  if n < 1:
    return [n]

  listSebelumN = fibonacci(n - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  return listSebelumN + [angka1 + angka2] 

def deret_aritmatika():
    a = int(input("Masukkan suku pertama yang diinginkan : "))
    b = int(input("Masukkan beda antar suku deret : "))
    f'Un = {a-b} + {b}n'
    Un=[]
    while True:
        n = int(input("Masukkan sampai suku ke berapa (n) : "))
        for n in range(1, n+1, 1):
            Un.append((a-b)+(b*n))
        return Un
    
def deret_kelipatan():
    a = int(input("Masukkan kelipatan berapa yang ingin dicari :"))
    b = int(input("Masukkan batas kelipatan perkalian awal : "))
    c = int(input("Masukkan batas kelipatan perkalian terakhir : "))
    for i in range(b, c+1):
        print(a*i, end=" ")  
    
menu_awal()
