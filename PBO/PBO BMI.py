class pasien : 
    #class variabel 
    jumlah_pasien = 0
    #konstruktor 
    def __init__(self, nama, berat, tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi 
        pasien.jumlah_pasien += 1
    #methode / fungsi 
    def bmi (self) :
        bmi = self.berat/ (self.tinggi**2)
        print ("BMI = ", bmi)
        if bmi < 18.5 :
            print ("Kekurangan berat badan.")
        elif bmi > 18.5 and bmi <= 24.9 :
            print ("Berat badan ideal.")
        elif bmi>24.9 and bmi <= 29.9 :
            print("Berat badan berlebih.")
        else : 
            print ("Obesitas.")
    
    def beratIdeal (self):
        ideal = (self.tinggi*100 - 100)-(10/100 * (self.tinggi*100 - 100))
        print("BB Ideal = ", ideal)
        print ("----------------------")

#instansiasi objek / pembuatan objek
pasien1 = pasien("Lizzy", 110, 1.7)
pasien2 = pasien ("Steff", 62, 1.65)
#pemanggilan pasien 1 
pasien1.bmi()
pasien1.beratIdeal()
#pemanggilan pasien 2
pasien2.bmi()
pasien2.beratIdeal()

print ("Jumlah Pasien : ", pasien.jumlah_pasien)