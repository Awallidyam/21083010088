# -*- coding: utf-8 -*-
"""TUGAS AKHIR SISOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O2WZH9BJe6kkMmn6As4QYcE19CPVC8OK
"""

def home():
    print("========================== Halo !!! ==========================")
    print("|                      Selamat Datang di                     |")
    print("================= PROGRAM DERET MATEMATIKA ===================")
    print("\nSilahkan Pilih Perhitungan yang Kamu inginkan")
    print("1. Deret Aritmatika")
    print("2. Deret Geometri")
    print("3. Deret Bilangan Ganjil")
    print("4. Deret Bilangan Genap")
    print("5. Deret Bilangan Prima")
    print("_"*62)
    pilihan = int(input("\nMasukkan pilihanmu dalam bentuk angka :"))      
    if pilihan == 1 :
        aritmatika()
    elif pilihan == 2 :
        geometri()
    elif pilihan == 3 :
        ganjil()
    elif pilihan == 4 :
        genap()
    elif pilihan == 5 :
        prima()
    else :
        print("Tidak ada perhitungan")


def aritmatika():
    print("\n=============== Halo !!! ===============")
    print("|           Selamat Datang di           |")
    print("======= PROGRAM DERET ARITMATIKA ========")
    print("\nSilahkan pilih perhitungan yang kamu inginkan")
    print("1. Suku ke-n")
    print("2. Jumlah suku ke-n")
    print("_"*62)
    program1=int(input("\nTentukan : "))
    if program1 == 1 :
        u1=int(input("\nMasukkan suku pertama : "))
        u2=int(input("Masukkan suku kedua: "))
        n=int(input("Banyak nya suku : "))
        b = u2 - u1
        Un = (u1+(n-1)*b)
        print("\nDari hasil inputan di dapatkan a =", u1, "sedangkan beda masing-masing suku =", b )
        print("Un :", Un)
        i = 1
        a = u1
        hasil = 0
        c = [u1, ]
        print("\nDeret :")
        while True :      
            if i < n :   
                i = i +1
                a = a + b
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\n")
        print("-"*62)
        lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))
        print("-"*62)
        print("\n")
        while(lanjut == "Y" or "y"):
            home()
        else:
            print("Ok dehh")
            
    elif program1 == 2 :
        u1=int(input("\nMasukkan suku pertama : "))
        u2=int(input("Masukkan suku kedua: "))
        n=int(input("Banyak nya suku : "))
        b = u2 - u1
        Un = (u1+(n-1)*b)
        Sn = (n/2*(u1+Un))
        print("\nDari hasil inputan di dapatkan a =", u1, "sedangkan beda masing-masing suku =", b, "dan nilai Un =", Un )
        i = 1
        a = u1
        hasil = 0
        c = [u1, ]
        print("\nDeret :")
        while True :      
            if i < n :   
                i = i +1
                a = a + b
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\nMaka jumlah Sn :", Sn)
        print("\n")
        print("_"*62)
        lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))   
        print("-"*62)
        print("\n")
        while(lanjut == "Y"or "y"):
            home()
        else:
            print("Ok dehh")
        
    else :
        print("Tidak ditemukan program aritmatika")
        
def geometri():
    print("\n=============== Halo !!! ===============")
    print("|           Selamat Datang di           |")
    print("======= PROGRAM DERET GEOMETRI ==========")
    print("\nSilahkan pilih perhitungan yang kamu inginkan:")
    print("1. Suku ke-n")
    print("2. Jumlah suku ke-n\n")
    print("_"*62)
    program2=int(input("\nTentukan :"))
    if program2 == 1 :
        u1=int(input("\nMasukkan suku pertama : "))
        u2=int(input("Masukkan suku kedua: "))
        n=int(input("Banyak nya suku : "))
        r = u2 / u1
        Un = (u1*r**(n-1))
        print("\nDari hasil inputan di dapatkan a =", u1, "sedangkan rasio masing-masing suku =", r )
        print("Un : ", Un)
        i = 1
        a = u1
        c = [u1, ]
        print("Deret :")
        while True :      
            if i < n :   
                i = i +1
                a = a * r
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\n")
        print("-"*62)
        lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))   
        print("-"*62)
        print("\n")
        while(lanjut == "Y" or "y"):
            home()
        else:
            print("Ok dehh")
        
    elif program2 == 2 :
        u1=int(input("\nMasukkan suku pertama : "))
        u2=int(input("Masukkan suku kedua: "))
        n=int(input("Banyak nya suku : "))
        r = u2 / u1
        Un = (u1*r**(n-1))
        Sn = (u1*r**n-1)/(r-1)
        print("\nDari hasil inputan di dapatkan a =", u1, "sedangkan rasio masing-masing suku =", r, "dan nilai Un =", Un )
        i = 1
        a = u1
        c = [u1, ]
        print("Deret :")
        while True :      
            if i < n :   
                i = i +1
                a = a * r
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\nMaka jumlah Sn : ", Sn)
        print("\n")
        print("-"*62)
        lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))   
        print("-"*62)
        print("\n")
        while(lanjut == "Y" or "y"):
            home()
        else:
            print("Ok dehh")
    else :
        print("Tidak ditemukan program geometri")

def ganjil():
    print("\n=============== Halo !!! ===============")
    print("|           Selamat Datang di           |")
    print("======= PROGRAM DERET ANGKA GANJIL ======")
    print("_"*62)
    awal = int(input("\nMasukkan angka awal :"))
    akhir = int(input("Masukkan angka akhir :"))
    print("\nDeret :")
    for i in range(awal, akhir+1) :
        if (i % 2 != 0):
            print(i, end=" ")
    print("\n")
    print("-"*62)
    lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))   
    print("-"*62)
    print("\n")
    while(lanjut == "Y" or "y"):
        home()
    else:
        print("Ok dehh")
        
def genap():
    print("\n=============== Halo !!! ===============")
    print("|           Selamat Datang di           |")
    print("======= PROGRAM DERET ANGKA GENAP =======")
    print("_"*62)
    awal = int(input("\nMasukkan angka awal :"))
    akhir = int(input("Masukkan angka akhir :"))
    print("\nDeret :")
    for i in range(awal, akhir+1):
        if (i % 2 == 0):
            print(i, end=" ")
    print("\n")
    print("-"*62)
    lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))  
    print("-"*62)
    print("\n")
    while(lanjut == "Y" or "y"):
        home()
    else:
        print("Ok dehh")
    
def prima():
    print("\n=============== Halo !!! ===============")
    print("|           Selamat Datang di           |")
    print("======= PROGRAM DERET ANGKA PRIMA =======")
    print("_"*62)
    angka_awal = int(input("\nMasukan angka awal: "))
    angka_akhir = int(input("Masukan angka akhir: "))

    list_angka = [i for i in range(angka_awal, angka_akhir +1 )]

    bilangan_prima = []
    for i in list_angka:
        if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
            bilangan_prima.append(i)
    print("\nDeret:")
    print(bilangan_prima)
    print("\n")
    print("-"*62)
    lanjut=(input("Apakah ingin lanjut ke perhitungan selanjutnya ? Y/N :"))   
    print("-"*62)
    print("\n")
    if lanjut == "Y" or "y":
        home()
    else:
        print("Ok dehh")

if __name__ == "__main__":
    home()
