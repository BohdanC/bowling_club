from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


root=Tk()
root.title("Пушка")
root.geometry('500x400')
root.resizable(False,False)
root.iconbitmap("12.ico")

combo=Combobox(root)
combo['values']=("Адміністратор","Офіціант","Бармен")
combo.current(0)
combo.grid(row=0,column=1)


myLabel1=Label(root,text="Введіть ім'я:").grid(row=1,column=1)
myLabel2=Label(root,text="Введіть вік:").grid(row=2,column=1)
myLabel3=Label(root,text="Введіть робочий час:").grid(row=3,column=1)
myLabel4=Label(root,text="Введіть номер телефону:").grid(row=4,column=1)

e1=Entry(root,width=30).grid(row=1,column=2)
e2=Entry(root,width=30).grid(row=2,column=2)
e3=Entry(root,width=30).grid(row=3,column=2)
e4=Entry(root,width=30).grid(row=4,column=2)

def clicked():
    messagebox.showinfo("Працівник створенний","?:\n")

myButton=Button(root,text="Створити працівника",command=clicked,fg="white",bg="black").grid(row=6,column=1)
exitButton=Button(root,text="Вийти",command=root.quit,fg="white",bg="red").grid(row=6,column=2)




root.mainloop()
