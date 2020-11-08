#File ini dibuat untuk Tugas Latihan 1 pada Modul pratikum 3

n=int(input("Masukkan Nilai N : "))
print("\n")
import random

for y in list(range(1, n+1, 1)):
    print("Data ke: ",y,"=>",random.uniform(0, 0.5))

print("selesai")
