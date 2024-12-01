import aritmatika_module as art
import bangundatar_module as bd
import bangunruang_module as br
def hitungan_aritmatika():
    print('\n Pilih operasi aritmatika yang ingin di lakukan')
    print('''
    1.Penambahan
    2.Pengurangan
    3.Perkalian
    4.Pembagian
    5.Pangkat      
    ----Luas Bangun Datar----
    6.Luas persegi
    7.Luas persegi panjang
    8.Luas segitiga
    9.Luas lingkaran
    10.Luas trapesium
    11.Luas jajargenjang
    12.Luas belahketupat
    13.Luas layang-layang
    ----Keliling Bangun Datar----
    14.keliling persegi
    15.keliling persegi panjang
    16.keliling segitiga
    17.keliling lingkaran
    18.keliling trapesium
    19.keliling jajargenjang
    20.keliling belahketupat
    21.keliling layang-layang
    ----Volume Bangun Ruang----
    22.volume kubus
    23.volume balok
    24.volume prismasegitiga
    25.volume kerucut
    26.volume bola
    ----luas permukaan Bangun Ruang----
    27.luas permukaan kubus
    28.luas permukaan balok
    29.luas permukaan prismasegitiga
    30.luas permukaan bola
    ----keliling Bangun Ruang----
    31.keliling kubus
    32.keliling balok
    33.keliling prismasegitiga
    ''')
    pilihan = int(input('\n Masukkan nomor operasi aritmatika yang di pilih (1-5) : '))

    if pilihan == 1:
        a = float(input('Masukkan angka Pertama: '))
        b = float(input('Masukkan angka Pertama: '))
        print('Hasil penambahan: ', art.tambah(a,b))
    elif pilihan ==2:
        a = float(input('Masukkan angka Pertama: '))
        b = float(input('Masukkan angka Pertama: '))
        print('Hasil Pengurangan: ', art.kurang(a,b))
    elif pilihan ==3:
        a = float(input('Masukkan angka Pertama: '))
        b = float(input('Masukkan angka Pertama: '))
        print('Hasil Perkalian: ', art.kali(a,b))
    elif pilihan ==4:
        a = float(input('Masukkan angka Pertama: '))
        b = float(input('Masukkan angka Pertama: '))
        if b == 0:
         return "Error: Pembagian dengan nol tidak diperbolehkan."
        else:
            print('Hasil Pembagian: ', art.bagi(a,b))
    elif pilihan ==5:
        a = float(input('Masukkan angka Pertama: '))
        b = float(input('Masukkan angka Pertama: '))
        if a < 0:
            return "Error: Akar kuadrat dari angka negatif tidak didefinisikan."
        else:
            print('Hasil pangkat: ', art.pangkat(a,b))
    if pilihan == 6:
        a = float(input('Masukkan sisi persegi: '))
        print('Hasil luas persegi adalah: ', bd.luas_persegi(a))
    elif pilihan ==7:
        a = float(input('Masukkan panjang: '))
        b = float(input('Masukkan lebar: '))
        print('Hasil luas persegi panjang adalah: ', bd.luas_persegipanjang(a,b))
    elif pilihan ==8:
        a = float(input('Masukkan alas segitiga: '))
        b = float(input('Masukkan tinggi segitiga: '))
        print('Hasil luas segitiga adalah: ', bd.luas_segitiga(a,b))
    elif pilihan ==9:
        a = float(input('Masukkan jari-jari lingkaran: '))
        print('Hasil luas lingkaran adalah: ', bd.luas_lingkaran(a))
    elif pilihan ==10:
        a = float(input('Masukkan sisi: '))
        b = float(input('Masukkan sisi: '))
        c = float(input('Masukkan tinggi: '))
        print('Hasil luas trapesium adalah: ', bd.luas_trapesium(a,b,c))
    elif pilihan ==11:
        a = float(input('Masukkan alas jajar genjang: '))
        b = float(input('Masukkan tinggi jajar genjang: '))
        print('Hasil luas jajar genjang adalah: ', bd.luas_jajargenjang(a,b))
    elif pilihan == 12:
        a = float(input('Masukkan diagonal pertama: '))
        b = float(input('Masukkan diagonal kedua: '))
        print('Hasil luas belah ketupat adalah: ', bd.luas_belahketupat(a,b))
    elif pilihan == 13:
        a = float(input('Masukkan diagonal pertama: '))
        b = float(input('Masukkan diagonal kedua: '))
        print('Hasil luas layang layang adalah: ', bd.luas_layang(a,b))
    if pilihan == 14:
        a = float(input('Masukkan sisi persegi: '))
        print('Hasil keliling persegi adalah: ', bd.keliling_persegi(a))
    elif pilihan ==15:
        a = float(input('Masukkan panjang: '))
        b = float(input('Masukkan lebar: '))
        print('Hasil keliling persegi panjang adalah: ', bd.keliling_persegipanjang(a,b))
    elif pilihan ==16:
        a = float(input('Masukkan sisi pertama: '))
        b = float(input('Masukkan sisi kedua: '))
        c = float(input('Masukkan sisi ketiga: '))
        print('Hasil keliling segitiga adalah: ', bd.keliling_segitiga(a,b,c))
    elif pilihan ==17:
        a = float(input('Masukkan jari-jari lingkaran: '))
        print('Hasil keliling lingkaran adalah: ', bd.keliling_lingkaran(a))
    elif pilihan ==18:
        a = float(input('Masukkan sisi pertama: '))
        b = float(input('Masukkan sisi kedua: '))
        c = float(input('Masukkan sisi ketiga: '))
        d = float(input('Masukkan sisi keempat: '))
        print('Hasil keliling trapesium adalah: ', bd.keliling_trapesium(a,b,c,d))
    elif pilihan ==19:
        a = float(input('Masukkan sisi jajar genjang: '))
        b = float(input('Masukkan lebar jajar genjang: '))
        print('Hasil keliling jajar genjang adalah: ', bd.keliling_jajargenjang(a,b))
    elif pilihan == 20:
        a = float(input('Masukkan sisi : '))
        print('Hasil keliling belah ketupat adalah: ', bd.keliling_belahketupat(a))
    elif pilihan == 21:
        a = float(input('Masukkan sisi pertama: '))
        b = float(input('Masukkan sisi kedua: '))
        print('Hasil keliling layang layang adalah: ', bd.keliling_layang(a,b))
    elif pilihan == 22:
        a = float(input('Masukkan sisi kubus: '))
        print('Hasil volume kubus adalah: ', br.volume_kubus(a))
    elif pilihan == 23:
        a = float(input('Masukkan panjang balok: '))
        b = float(input('Masukkan lebar balok: '))
        c = float(input('Masukkan tinggi balok: '))
        print('Hasil volume balok adalah: ', br.volume_balok(a,b,c))
    elif pilihan == 24:
        a = float(input('Masukkan alas prismasegitiga: '))
        b = float(input('Masukkan tinggi segitiga: '))
        c = float(input('Masukkan tinggi prisma: '))
        print('Hasil volume prismasegitiga adalah: ', br.volume_prismasegitiga(a,b,c))
    elif pilihan == 25:
        a = float(input('Masukkan jari jari kerucut: '))
        b = float(input('Masukkan tinggi kerucut: '))
        print('Hasil volume kerucut adalah: ', br.volume_kerucut(a,b))
    elif pilihan == 26:
        a = float(input('Masukkan jari jari bola: '))
        print('Hasil volume bola adalah: ', br.volume_bola(a))  
    elif pilihan == 27:
        a = float(input('Masukkan sisi kubus: '))
        print('Hasil luas permukaan kubus adalah: ', br.lp_kubus(a))
    elif pilihan == 28:
        a = float(input('Masukkan panjang balok: '))
        b = float(input('Masukkan lebar balok: '))
        c = float(input('Masukkan tinggi balok: '))
        print('Hasil luas permukaan balok adalah: ', br.lp_balok(a,b,c))
    elif pilihan == 29:
        a = float(input('Masukkan alas : '))
        b = float(input('Masukkan tinggi segitiga: '))
        c = float(input('Masukkan sisi satu: '))
        d = float(input('Masukkan sisi dua: '))
        e = float(input('Masukkan tinggi prisma: '))
        print('Hasil luas permukaan prismasegitiga adalah: ', br.lp_prismasegitiga(a,b,c,d,e))
    elif pilihan == 30:
        a = float(input('Masukkan jari jari bola: '))
        print('Hasil luas permukaan bola adalah: ', br.lp_bola(a))
    elif pilihan == 31:
        a = float(input('Masukkan sisi kubus: '))
        print('Hasil keliling kubus adalah: ', br.keliling_kubus(a))
    elif pilihan == 32:
        a = float(input('Masukkan panjang balok: '))
        b = float(input('Masukkan lebar balok: '))
        c = float(input('Masukkan tinggi balok: '))
        print('Hasil keliling balok adalah: ', br.keliling_balok(a,b,c))
    elif pilihan == 33:
        a = float(input('Masukkan alas : '))
        b = float(input('Masukkan sisi satu: '))
        c = float(input('Masukkan sisi dua: '))
        print('Hasil keliling prismasegitiga adalah: ', br.keliling_prismasegitiga(a,b,c))
 
    else:
        print('Pilihan tidak valid')
    
    
        
hitungan_aritmatika()