from abc import ABC, abstractmethod
import math

# Abstract class BangunRuang
class BangunRuang(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def luas_permukaan(self):
        pass

# Class Turunan Kubus
class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

    def luas_permukaan(self):
        return 6 * (self.sisi ** 2)

# Class Turunan Bola
class Bola(BangunRuang):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def luas_permukaan(self):
        return 4 * math.pi * self.radius ** 2

# Implementasi program
def main():
    print("Pilih bangun ruang yang ingin dihitung:")
    print("1. Kubus")
    print("2. Bola")
    
    pilihan = int(input("Masukkan pilihan (1 atau 2): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        kubus = Kubus(sisi)
        print("\nHasil Perhitungan Kubus:")
        print(f"Volume Kubus: {kubus.volume()}")
        print(f"Luas Permukaan Kubus: {kubus.luas_permukaan()}")
    elif pilihan == 2:
        radius = float(input("Masukkan radius bola: "))
        bola = Bola(radius)
        print("\nHasil Perhitungan Bola:")
        print(f"Volume Bola: {bola.volume()}")
        print(f"Luas Permukaan Bola: {bola.luas_permukaan()}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
