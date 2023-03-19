nilai = int(input("Masukkan nilai : "))

if (nilai >= 90) :
    print("Predikat A")
elif (nilai >= 80) and (nilai < 90):
    print("Predikat B")
elif (nilai >= 60) and (nilai < 80):
    print("Predikat C")
elif (nilai >= 40) and (nilai < 60):
    print("Predikat D")
else:
    print("Predikat E")
    
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak lulus")
    