from tkinter import *

window = Tk()
window.title("Form Data Warga Negara Indonesi | Python Programing | Kelompok 3")

def cetak():
    nik = fnik.get()
    nama = fnama.get()
    jk = str(var.get())

    print("NIK : ",nik)
    print("Nama : ",nama)
    print("Jenis Kelamin : ",jk)

frame1 = Frame(window, bg='#116fa5', width=800, height=100)
frame1.pack()
frame1.pack_propagate(0)
klp4 = Label(frame1, text="Kelompok 3", bg='#116fa5')
klp4.pack(side=TOP, expand=YES)
Font_klp4 = ("Arial", 17, "bold")
klp4.configure(font = Font_klp4)

judul = Label(frame1,text="DATA WARGA NEGARA REPUBLIK INDONESIA",bg='#116fa5', fg="black")
judul.pack(side=BOTTOM, expand=YES)
Font_judul = ("Arial", 15, "bold")
judul.configure(font = Font_judul)

frame2 = Frame(window, bg='#2fa5c9', width=800, height=500)
frame2.pack()
frame2.grid_propagate(0)

nik = Label(frame2, text="NIK",bg='#2fa5c9', fg="white",font=11)
nik.grid(row=0,column=0, padx=120, pady=10)
fnik = Entry(frame2)
fnik.insert(0,"760402...")
fnik.grid(row=0,column=1, ipadx=60)

nama = Label(frame2, text="Nama Lengkap",bg='#2fa5c9', fg="white",font=11).grid(row=1, column=0,pady=10)
fnama = Entry(frame2)
fnama.insert(0,"Nama Sesuai KTP")
fnama.grid(row=1, column=1,ipadx=60)

var = StringVar()
jk = Label(frame2, text="Jenis Kelamin",bg='#2fa5c9', fg="white",font=11).grid(row=2, column=0,pady=10)
l = Radiobutton(frame2,text="LAKI-LAKI", variable=var, value="Laki-Laki",bg='#2fa5c9', fg="black").grid(row=2,column=1,ipadx=60)
p = Radiobutton(frame2,text="PEREMPUAN",variable=var, value="Perempuan",bg='#2fa5c9', fg="black").grid(row=3,column=1,ipadx=60)

gd = Label(frame2, text="Golongan Darah",bg='#2fa5c9', fg="white",font=11).grid(row=4, column=0)
ListB = Listbox(frame2)
ListB.insert(1, "A")
ListB.insert(2, "B")
ListB.insert(3, "AB")
ListB.insert(4, "O")
ListB.insert(5, "Tidak Tahu")
ListB.grid(row=4,column=1,pady=20)

ttl = Label(frame2, text="Tempat/Tanggal Lahir",bg='#2fa5c9', fg="white",font=11).grid(row=5, column=0,pady=10)
tempat = Entry(frame2)
tempat.insert(0,"Tempat...")
tempat.grid(row=5, column=1)
tgl = Spinbox(frame2, from_=0, to=31, width=3).grid(row=5, column=2,padx=10)
bulan = Spinbox(frame2, from_=0, to=12, width=3).grid(row=5, column=3,padx=10)
tahun = Entry(frame2)
tahun.insert(0,"Tahun...")
tahun.grid(row=5, column=4)

alamat = Label(frame2, text="Alamat",bg='#2fa5c9', fg="white",font=11).grid(row=6, column=0,pady=30)
falamat = Text(frame2, width=30,height=3)
falamat.grid(row=6,column=1)

frame3 = Frame(window, bg='#116fa5', width=800, height=670)
frame3.pack()
frame3.grid_propagate(0)

reset = Button(frame3,text="Reset form", bg="red",fg="white").grid(row=1,column=4,ipadx=100,padx=100,ipady=4,pady=11)
kirim = Button(frame3,text="Kirim",bg="blue",fg="white",command=cetak).grid(row=1,column=5,ipadx=100,ipady=4,pady=11)
window.mainloop()
