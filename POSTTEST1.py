print ("MENGHITUNG VOLUME BANGUN RUANG")
print ("______________________________")

#login sederhana
username = input("Masukkan nama  : ")
nim = input("Masukkan NIM   : ")
kelas = input("Masukkan kelas : ")

print("________________________________________________________________")
print("login berhasil, silahkan memilih bangun ruang yang akan dihitung")
print("________________________________________________________________")

print("Pilihan operasi")
print("1. bola")
print("2. tabung")
print("3. limas segitiga")

operasi = int(input("masukkan pilihan operasi(1/2/3) : "))

if operasi == 1:
    r = float(input("masukkan nilai jari-jari : "))
    operasi = input("dapat dibagi 7 atau tidak dapat dibagi 7 :")
if operasi == "dapat dibagi 7" :
    v = 4*22/7*r*r
    print ("volume bola adalah : ", v)
elif operasi == "tidak dapat dibagi 7" :
    v = 4/3*3.14*r*r*r
    print ("volume bola adalah : ", v)

if operasi == 2:
    t = int(input("masukkan tinggi : "))
    r = int(input("masukkan jari-jari : "))
    operasi = input("dapat dibagi 7 atau tidak dapat dibagi 7 :")
if operasi == "dapat dibagi 7" :
    v = 22/7 * r * r * t
    print ("volume tabung adalah : ", v)
elif operasi == "tidak dapat dibagi 7" :
    v = 3.14* r * r * t
    print ("volume tabung adalah : ", v)

elif operasi == 3:
    la = int(input("masukkan luas alas : "))
    ts = int(input("masukkan tinggi sisi : "))
    v = 1/3*(la*ts)
    print("volume limas segitiga adalah : ", v) 
    




