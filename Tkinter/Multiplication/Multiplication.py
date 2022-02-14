from tkinter import *

Multiply = Tk()
Multiply.title(" Multiplication Table ")
#Multiply.geometry('490x950')
Multiply.resizable(0,0)
Multiply.configure(background="green")

input_text=StringVar()

def Calc():
    textDisplay.delete("1.0", "end")
    for x in range(1, 13):
        m = float(input_text.get())
        textDisplay.insert(END, (x), '\t'," x ", '\t', (m) , '\t' , " = ", '\t', (x*m))
        textDisplay.insert((END),'\n\n')


lblTable=Label(Multiply, text="Table Multiplication", font=('arial',20,'bold'), fg='green')
lblTable.grid(row=0, column=0)

txtInput = Entry(Multiply, textvariable=input_text, bd=30, font=('arial',20,'bold'), justify='center', width=13)
txtInput.grid(row=1, column=0)

btnCalc=Button(Multiply,font=('arial',20,'bold'), text="Calc",fg='green', width=13, command=Calc)
btnCalc.grid(row=2,column=0)

textDisplay = Text(Multiply, width=30, height= 23, bd=16, font=('arial',20,'bold'))
textDisplay.grid(row=3,column=0)


Multiply.mainloop()

