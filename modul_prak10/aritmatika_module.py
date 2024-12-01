import math

def tambah(a,b):
    return a+b
def kurang(a,b):
    return a-b
def kali(a,b):
    return a*b
def bagi(a,b):
    if b == 0: 
        return"error: Pembagian nol tidak di perbolehkan."
    else:
        return a/b
    
def pangkat(a,b):
    return math.pow(a,b)
    
def eksponensial(a,b):
    return a**b

def akar_kuadrat(a,b):
    if b < 0: 
        return"error: akar kuadrat dari angka negatif tidak di definisikan"
    else:
        return math.sqrt(a)
    