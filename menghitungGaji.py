nama = input("Masukkan Nama : ")
golongan = input("Golongan Kerja : ")
jam = int(input("Masukkam Jam Kerja : "))
print("1.SMA \n2. D1 \n3. D3 \n4. S1")
golpen = input("Masukkan Pendidikan \t: ")
gaji = 300000

if golongan == "1":
    upah = 0.05*gaji
elif golongan == "2":
    upah = 0.10*gaji
elif golongan == "3":
    upah = 0.15*gaji
else:
    upah = 0
    
if golpen == "SMA":
    tunpen = 0.025*gaji
elif golpen == "D1":
    tunpen = 0.05*gaji
elif golpen == "D3":
    tunpen = 0.20*gaji
elif golpen == "S1":
    tunpen = 0.30*gaji
else:
    tunpen = 0
    
if jam > 8:
    lembur = jam - 8
    hlembur = lembur * 3500
else :
    hlembur = 0
    
total = tunpen + upah + gaji + hlembur

print("\n")
print("=============================================================================")
print("")
print("\t\t\t Program Menghitung Gaji Karyawan")
print("\n")
print("=============================================================================")
print("Nama \t\t\t\t: ", nama)
print("Golongan Kerja \t\t\t: ", golongan)
print("Jumlah Jam Kerja \t\t: ", jam)
print("Pendidikan \t\t\t: ", golpen)
print("Gaji Pokok \t\t\t: ", gaji)
print("Tunjangan Jabatan \t\t: ",upah)
print("Tunjangan Pendidikan \t\t: ", tunpen)
print("Bonus Lembur \t\t\t: ", hlembur)
print("Total Gaji dan Tunjangan \t: ", total)
