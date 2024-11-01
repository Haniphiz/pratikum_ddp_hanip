# tugas satu
kendaraan = ['beat', 'motor', 200 , 'merah',  2]

kendaraan.append('13 juta')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

rumus_luas = int(input('''pilih antara |` 1 | 2 | 3 | =
                   1.hitung luas persegi
                   2.hitung luas lingkaran
                   3.hitung luas segitiga 
                       = '''))
match rumus_luas:
    case 1:
        print(' menghitung luas persegi')
        sisi =int(input('masukkan sisi = '))
        luas_persegi = sisi**2
        print(f'luas persegi adalah {luas_persegi}')
    case 2:
        print(' menghitung luas lingkaran')
        jari_lingkaran = int(input(' masukkan jari jari lingkaran = '))
        luas_lingkaran = 3.14 * (jari_lingkaran * jari_lingkaran)
        print(f'luas lingkaran adalah {luas_lingkaran}')
    case 3:
        print(' menghitung luas segitiga')
        alas_segitiga = int(input('masukkan alas segitiga = '))
        tinggi_segitiga = int(input('masukkan tinggi segitiga = '))
        luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
        print(f'luas segitiga adalah {luas_segitiga}')
    case _:
        print('pilihan tidak valid')

