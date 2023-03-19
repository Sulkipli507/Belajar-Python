while True :
    bilangan = int(input("Masukkan bilangan : "))
    if bilangan ==0:
        print("Program selesai")
        break
    elif bilangan%3==0 and bilangan%7==0:
        print("Faktor 3 dan 7")
    elif bilangan%3==0:
        print("Faktor 3")
    elif bilangan%7==0:
        print("Faktor 7")
    else:
        print("None")