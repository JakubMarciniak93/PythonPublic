from tkinter import *

root = Tk()
root.title("Simple Calc")

inputfieled=Entry(root, width = 35, borderwidth=5)
inputfieled.grid(row=0, column=0, columnspan=3 ,padx=10, pady=10)

def button_click(number):
    #zmienna bierze wartość z pola
    current = inputfieled.get()
    #usuwamy wartość z pola
    inputfieled.delete(0, END)
    #sumujemy wartość ze zmiennej i nowe dane z pola
    inputfieled.insert(0,str(current) +str(number) )

def button_clear():
    inputfieled.delete(0, END)

def button_add():
    #pobieramy pierwszą wartość z pola
    first_number=inputfieled.get()
    #tworzymy global pierwszą wartość
    global f_num
    #zmienna math określająca działanie
    global math
    math = "add"
    #przypisujemy do globala wartość z zmiennej przechowującej wpis z pola
    f_num=int(first_number)
    #czyścimy pole
    inputfieled.delete(0, END)

def button_equel():
    second_number = inputfieled.get()
    inputfieled.delete(0, END)
    if math == "add":
        inputfieled.insert(0,f_num + int(second_number))

    elif math == "sub":
        inputfieled.insert(0, f_num - int(second_number))

    elif math == "mult":
        inputfieled.insert(0, f_num * int(second_number))

    elif math == "dev":
        inputfieled.insert(0, f_num / int(second_number))

def button_subtractr():
    first_number = inputfieled.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    inputfieled.delete(0, END)

def button_multiply():
    first_number = inputfieled.get()
    global f_num
    global math
    math = "mult"
    f_num = int(first_number)
    inputfieled.delete(0, END)

def button_devide():
    first_number = inputfieled.get()
    global f_num
    global math
    math = "dev"
    f_num = int(first_number)
    inputfieled.delete(0, END)

button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add= Button(root, text="+", padx=40, pady=20, command= button_add)
button_equel= Button(root, text="=", padx=85, pady=20, command=button_equel)
button_clear= Button(root, text="C", padx=85, pady=20, command=button_clear)
button_subtractr= Button(root, text="-", padx=41, pady=20, command=button_subtractr)
button_multiply= Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_devide= Button(root, text="/", padx=39, pady=20, command=button_devide)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

button_0.grid(row=4 , column=0)
button_clear.grid(row=4 , column=1, columnspan=2)
button_add.grid(row=5 , column=0)
button_equel.grid(row=5 , column=1, columnspan=2)

button_subtractr.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_devide.grid(row=6, column=2)

root.mainloop()