from tkinter import*
from tkinter import messagebox,ttk
import random

root=Tk()
root.title('Form tiket')
root.geometry('1280x720')
root.resizable(False,False)
bg_color='#008B8B'

city = ['Majene','Tinambung', 'Balanipa','Campalagian','Mapilli',
        'Tapango','Wonomulyo','Polewali']

dict={	'Majene-Tinambung':3000,
        'Majene-Balanipa ':5000,
        'Majene-Campalagian':7000,
        'Majene-Mapilli':10000,
        'Majene-Tapango':12000,
        'Majene-Wonomulyo':15000,
        'Majene-Polewali':20000,
		'Tinambung-Balanipa':3000,
		'Tinambung-Campalagian':5000,
		'Tinambung-Mapilli':7000,
		'Tinambung-Tapango':10000,
		'Tinambung-Wonomulyo':12000,
		'Tinambung-Polewali':17000,
        'Balanipa-Campalagian':3000,
        'Balanipa-Mapilli':5000,
        'Balanipa-Tapango':7000,
        'Balanipa-Wonomulyo':10000,
        'Balanipa-Polewali':15000,
        'Campalagian-Mapilli':4000,
        'Campalagian-Tapango':8000,
        'Campalagian-Wonomulyo':120000,
        'Campalagian-Polewali':12000,
        'Mapilli-Tapango':5000,
        'Mapilli-Wonomulyo':8000,
        'Mapilli-Polewali':1000,
        'Tapango-Wonomulyo':5000,
        'Tapango-Polewali':7000,
        'Wonomulyo-Polewali':80000
}
#=================variables================
person=IntVar()
c_name=StringVar()
c_phone=StringVar()
ticket_no=StringVar()
#======================================Frames=================

def varify():
    global dis
    a = combo_s.get()
    b = combo_d.get()
    p = person.get()
    d=a+'-'+b
    e=b+'-'+a
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
            messagebox.showerror('Error','Masukkan nomor telfon yang valid')
            return
    else:
        messagebox.showerror("Error", "Detail Pemesan harus diisi !")
        return
    if a!=b:
        if d in dict:
            dis= dict[d]
        elif e in dict:
            dis = dict[e]
    else:
        messagebox.showwarning('Warning ','Asal harus diiisi')
        return
    messagebox.showinfo('Veritifikasi','Berhasil Diverifikasi')

def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END,f"\n {55*'*'}")
        textarea.insert(END, f"\n\n Asal :\t\t      {combo_s.get()}")
        textarea.insert(END, f"\n Tujuan :\t\t      {combo_d.get()}")
        textarea.insert(END, f"\n {p} pemesan ")
        textarea.insert(END, f"\nBiaya perjalanan :\t\tRp. {dis}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\nJumlah :\t\tRp. {p*dis}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n\n {55*'*'}")
    except Exception:
        messagebox.showwarning('Warning','Tolong verititfikasi tiket dahulu')
        clear()

def clear():
    c_name.set('')
    c_phone.set('')
    combo_s.set('Pilih Asal')
    combo_d.set('Pilih Tujuan')
    person.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Anda yakin ingin keluar?")
    if op > 0:
        root.destroy()



def welcome():
    x = random.randint(1000, 9999)
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t  Happy journey")
    textarea.insert(END,f"\n\nNomor Tiket:\t\t {    ticket_no.get()}")
    textarea.insert(END,f"\nNama Pemesan:\t\t  {    c_name.get()}")
    textarea.insert(END,f"\nNomor Telfon:\t\t    {    c_phone.get()}")
    textarea.configure(font='arial 15 bold')

title=Label(root,pady=2,text="Pemesanan Tiket Kereta",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Detail Pemesan',font=('times new romon',15,'bold'),fg='#AFEEEE',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Nama Pemesan',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='No Telfon. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Detail Tiket', font=('times new romon', 18, 'bold'), fg='#AFEEEE',bg=bg_color)
F2.place(x=20, y=180,width=630,height=500)

source= Label(F2, text='Asal', font=('times new roman',19, 'bold'), bg=bg_color, fg='#F0FFFF').grid(
row=0, column=0, padx=30, pady=20)
combo_s=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=city)
combo_s.grid(row=0,column=1,pady=10)
combo_s.set('Pilih Asal')

des= Label(F2, text='Tujuan', font=('times new romon',18, 'bold'), bg=bg_color, fg='#F0FFFF').grid(
row=1, column=0, padx=30, pady=20)
combo_d=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=city)
combo_d.grid(row=1,column=1,pady=10)
combo_d.set('Pilih Tujuan')

n= Label(F2, text='Jumlah Tiket', font=('times new romon',18, 'bold'), bg=bg_color, fg='#F0FFFF').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Spinbox(F2, width=20,textvariable=person, font='arial 15 bold', relief=SUNKEN, bd=7, from_= 0, to = 25).grid(row=2, column=1, padx=10,pady=20)
#n_txt = Spinbox(F2, width=20, from_= 0, to = 25, ).grid(row=2, column=1, padx=10,pady=20)

#========================Ticket area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Tiket',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Veritifikasi',font='arial 15 bold',command=varify,padx=5,pady=10,bg='#F0FFFF',width=15, activebackground='#00FA9A')
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Tiket',font='arial 15 bold',command=gticket,padx=5,pady=10,bg='#F0FFFF',width=15, activebackground='#00FA9A')
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='#F0FFFF',width=15, activebackground='#00FA9A')
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='#DC143C',width=15, activebackground='#00FA9A')
btn4.grid(row=4,column=1,padx=10,pady=30)

root.mainloop()
