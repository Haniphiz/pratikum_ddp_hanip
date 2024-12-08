# memanggil file gempa dan import semua method

from gempa import *

# membuat objek gempa dengan argumen
gempa1 = gempa('banten', 1.2)
gempa2 = gempa('palu', 6.1)
gempa3 = gempa('cianjur', 5.6)
gempa4 = gempa('jayapura', 3.3)
gempa5 = gempa('jayapura', 4.0)

# informasi gempa
print('## info gempa maehh ##')
print()
gempa1.dampak()

print('## info gempa maehh ##')
print()
gempa2.dampak()

print('## info gempa maehh ##')
print()
gempa3.dampak()

print('## info gempa maehh ##')
print()
gempa4.dampak()

print('## info gempa maehh ##')
print()
gempa5.dampak()
