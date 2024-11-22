# 1. mengembalikan suhu yang dikonversi ke Fahrenheit


def celcius_ke_fahrenheit(celcius):
    print((9/5 * celcius) + 32)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)


#  Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.

def is_genap(nilai):
    if nilai % 2 == 0:
        print('True')
    else:
        print('False')

is_genap(4)
is_genap(7)

# 3. Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus :
def nilai(poin):
    if poin >= 80:
        print("lulus")
    elif poin <= 60:
        print('gagal')
    else:
        print('ini tidak valid')
nilai(80)
nilai(60)
        
# 4. fungsi untuk menampilkan bilangan ganjil yang kurang argumens bilangan(20)
 
def ganjil(bilangan):
    return[i for i in range (1, bilangan, 2)]
print(ganjil(20))

