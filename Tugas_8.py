# Memuat built-in libraries yang akan digunakan
from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process

# Inisialisasi function yang akan digunakan
def cetak(a):
    bilangan = a % 2
    if bilangan == 0:
        print(a, "Genap - ID proses", getpid())
    else:
        print(a, "Ganjil - ID proses", getpid())
    sleep(1)

# Input bilangan
x = int(input("Input bilangan acuan: "))

# Pemrosesan Sekuensial
print("\nPemrosesan Sekuensial")
sekuensial_awal = time()

for a in range(1, x + 1):
    cetak(a)
sekuensial_akhir = time()

# Multiprocessing Process
print("\nMultiprocessing dengan multiprocessing.Process")

kumpulan_proses = []
process_awal = time()

for a in range(1, x + 1):
    p = Process(target=cetak, args=(a,))
    kumpulan_proses.append(p)
    p.start()

for a in kumpulan_proses:
    p.join()

process_akhir = time()

# Multiprocessings Pool
print("\nMultiprocessing dengan multiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(1, x + 1))
pool.close()

pool_akhir = time()

# Perbandingan waktu eksekusi
print("\nWaktu eksekusi sekuensial              :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool    :", pool_akhir - pool_awal, "detik")
