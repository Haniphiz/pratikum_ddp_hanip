def volume_kubus(a):
    return a**3
def volume_balok(a,b,c):
    return a*b*c
def volume_prismasegitiga(a,b,c):
    return ((a*b)/2)*c
def volume_kerucut(a,b):
    return (1/3)*3.14*a**2*b
def volume_bola(a):
    return 4/3*3.14*a**3
def lp_kubus(a):
    return 6*(a*a)
def lp_balok(a,b,c):
    return 2*((a*b)+(a*c)+(b*c))
def lp_prismasegitiga(a,b,c,d,e):
    luas_alas=0.5*a*b
    keliling_alas=a+c+d
    return (2*luas_alas) + (keliling_alas*e)
def lp_bola(a):
    return 4*3.14*a**2
def keliling_kubus(a):
    return 12*a
def keliling_balok(a,b,c):
    return 4*(a+b+c)
def keliling_prismasegitiga(a,b,c):
    return a+b+c
