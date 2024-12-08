class gempa:
    #konstraktor inisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):
        #atribut
        self.lokasi = lokasi
        self.skala = skala

    # method menentukan dampak skala gempa
    def dampak(self):
        # logika
        if self.skala < 2:
            print('dampak gempa tidak berasa')
        elif self.skala >=2 and self.skala <=4:
            print(' dampak gempa bangunan retak-reta')
        elif self.skala >=4 and self.skala <=6:
            print('  dampak gempa bangunan roboh')
        elif self.skala > 6:
            print(' dampak gempa bangunan roboh dan berpotensi tsunami')

        
        # manammpilkan lokasi dan skala
        print(f' lokasi gempa : {self.lokasi}')
        print(f' skala gempa : {self.skala}')