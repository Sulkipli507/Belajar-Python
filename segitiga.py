a = int(input("Masukkan nilai: "))
s = 2 * a - 2
for i in range(1, a):
    for j in range(1, s):
        print(" ", end=" ")
    s -= 2
    for j in range(1, i+1):
        print(j," ", end=" ")
    print(" ")
    
print("\n")  
    
s = 1
for i in range(1, a):
    for j in range(1, s):
        print(' ', end=' ')
    s += 2
    for j in range(1, a):
        print(j,' ', end=' ')
    a -= 1
    print(' ')

print("\n")

s = a - 1
for i in range(1, a):
    for j in range(1, s):
        print(' ',end=' ')
    s -= 1
    for j in range(1, i+1):
        print('*', end=' ')
    print(' ')
