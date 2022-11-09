from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
	if i%2 == 0:
		print(i+1, "Ganjil - ID proses", getpid())
	else:
		print(i+1, "Genap - ID proses", getpid())
	sleep(1)

jumlah = int(input("input : "))


#sekuensial
print("SEKUENSIAL")
sekuensial_awal = time()

for i in range(jumlah):
	cetak(i)

sekuensial_akhir = time()

#process
print("MULTIPROCESSING.PROCESS")
kumpulan_proses = []

process_awal = time()

for i in range(jumlah):
	p = Process(target=cetak, args=(i,))
	kumpulan_proses.append(p)
	p.start()

for i in kumpulan_proses:
	p.join()

process_akhir = time()

#pool
print("MULTIPROCESSING.POOL")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(0, jumlah))
pool.close()

pool_akhir = time()

#membandingkanwaktu
print("MEMBANDINGKAN WAKTU")
print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool:", pool_awal, "detik")
 
