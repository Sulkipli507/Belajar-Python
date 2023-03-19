baris = int(input("Masukkan nilai yang diinginkan :"))
for i in range (1,baris):
    for j in range (1, i+1):
        print(j, end=" ")
    print("")
    
for angka in range(baris):
    for i in range(angka):
        print(angka, end=" ")
    print("")
    
for i in range (baris, 0, -1):
    angka = i
    for j in range(0,i):
        print(angka, end=" ")
    print("")