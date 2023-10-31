print('''
Slahkan pilih nomor dibawah ini
untuk menggunakan tools dibawah ini
===================
PILIHAN
===================
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga''')

keterangan = int(input("hitung hasil : "))

match keterangan:
    case 1:
        Luas_Persegi = int(input("masukkan nilai sisi : "))
        Hasil_Luas = Luas_Persegi * Luas_Persegi
        print("Luas Persegi adalah", Hasil_Luas)
    
    case 2:
        Nilai_pi = float(input("masukkan nilai Pi : "))
        Nilai_Jari = int(input("masukkan nilai Jari Jari : "))
        JariJari = Nilai_Jari * Nilai_Jari
        Luas_Lingkaran = Nilai_pi * JariJari
        print("Luas Lingkaran Adalah :", Luas_Lingkaran)
    
    case 3:
        setengah = float(0.5)
        Alas = int(input("masukkan nilai Alas :"))
        Tinggi = int(input("masukkan nilai Tinggi :"))
        Hasil_Luas = setengah * Alas * Tinggi
        print("Luas Segitiga Adalah :", Hasil_Luas)
    case _:
        print("tester")