
import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("======================")
print("   GAME TEBAK ANGKA")
print("======================")
print("Tebak angka dari 1 sampai 100!")

while True:
    tebak = int(input("Masukkan tebakan: "))
    percobaan += 1

    if tebak < angka_rahasia:
        print("Terlalu kecil!")
    elif tebak > angka_rahasia:
        print("Terlalu besar!")
    else:
        print("BENAR! Kamu menang!")
        print("Jumlah percobaan:", percobaan)
        break
