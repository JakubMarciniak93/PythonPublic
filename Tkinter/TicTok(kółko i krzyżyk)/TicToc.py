import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1100x700")
root.title(" Tic Toc ")
root.configure(background="green")

MainWindows=Frame(root, bd=10, width=600, height=680, relief=RIDGE,background="green")
MainWindows.pack()

TitleFrame=Frame(MainWindows, bd=5, width=600, height=80, relief=RIDGE)
TitleFrame.grid(row=0,column=0)

GameFrame=Frame(MainWindows, bd=5, width=600, height=300, relief=RIDGE, background="green")
GameFrame.grid(row=1,column=0)

LeftFrame=Frame(GameFrame, bd=15, width=300, height=300, relief=RIDGE)
LeftFrame.grid(row=1,column=0)

RightFrame=Frame(GameFrame, bd=5, width=300, height=300, relief=RIDGE)
RightFrame.grid(row=1,column=1)

PointsFrame=Frame(RightFrame, bd=5, width=300, height=150, relief=RIDGE)
PointsFrame.grid(row=0,column=0)

ButtonFrame=Frame(RightFrame, bd=5, width=300, height=150, relief=RIDGE)
ButtonFrame.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()
PlayerTurn=StringVar()

PlayerX.set(0)
PlayerO.set(0)

buttons=StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        PlayerTurn.set("PlayerO")
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        PlayerTurn.set("PlayerX")
        scorekeeper()

def next_game():
    button1['text']= " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

def reset_game():
    next_game()
    PlayerX.set(0)
    PlayerO.set(0)

def scorekeeper():
    if (button1['text']=="X" and button2['text']=="X" and button3['text']=="X"):
        button1.configure(background="lightgreen")
        button2.configure(background="lightgreen")
        button3.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button4['text']=="X" and button5['text']=="X" and button6['text']=="X"):
        button4.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button6.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button7['text']=="X" and button8['text']=="X" and button9['text']=="X"):
        button7.configure(background="lightgreen")
        button8.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button3['text']=="X" and button5['text']=="X" and button7['text']=="X"):
        button3.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button7.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button1['text']=="X" and button5['text']=="X" and button9['text']=="X"):
        button1.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button1['text']=="X" and button4['text']=="X" and button7['text']=="X"):
        button1.configure(background="lightgreen")
        button4.configure(background="lightgreen")
        button7.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button2['text']=="X" and button5['text']=="X" and button8['text']=="X"):
        button2.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button8.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button3['text']=="X" and button6['text']=="X" and button9['text']=="X"):
        button3.configure(background="lightgreen")
        button6.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

#=============================================OOOOOOOOOOOOOOO===================================
    if (button1['text']=="O" and button2['text']=="O" and button3['text']=="O"):
        button1.configure(background="lightgreen")
        button2.configure(background="lightgreen")
        button3.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

    if (button4['text']=="O" and button5['text']=="O" and button6['text']=="O"):
        button4.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button6.configure(background="lightgreen")
        n= float(PlayerXO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

    if (button7['text']=="O" and button8['text']=="O" and button9['text']=="O"):
        button7.configure(background="lightgreen")
        button8.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

    if (button3['text']=="O" and button5['text']=="O" and button7['text']=="O"):
        button3.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button7.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

    if (button1['text']=="O" and button5['text']=="O" and button9['text']=="O"):
        button1.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button1['text']=="O" and button4['text']=="O" and button7['text']=="O"):
        button1.configure(background="lightgreen")
        button4.configure(background="lightgreen")
        button7.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner X", "You won this time")
        next_game()

    if (button2['text']=="O" and button5['text']=="O" and button8['text']=="O"):
        button2.configure(background="lightgreen")
        button5.configure(background="lightgreen")
        button8.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

    if (button3['text']=="O" and button6['text']=="O" and button9['text']=="O"):
        button3.configure(background="lightgreen")
        button6.configure(background="lightgreen")
        button9.configure(background="lightgreen")
        n= float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You won this time")
        next_game()

lblPlayerX=Label(PointsFrame, font=('arial',40,'bold'), text="Player X : ", padx=2,pady=2)
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX=Entry(PointsFrame, font=('arial',40,'bold'), bd=2, fg="black" , textvariable= PlayerX, width=5, justify=LEFT)
txtPlayerX.grid(row=0, column =1 )

lblPlayerO=Label(PointsFrame, font=('arial',40,'bold'), text="Player O : ", padx=2,pady=2)
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO=Entry(PointsFrame, font=('arial',40,'bold'), bd=2, fg="black" , textvariable= PlayerO, width=5, justify=LEFT)
txtPlayerO.grid(row=1, column =1 )

buttonReset=Button(ButtonFrame, text="Next Game", font=('Times 26 bold'), height=3, width=15, bg='gainsboro', command=next_game)
buttonReset.grid(row=0, column=0, sticky=E+W)
buttonReset=Button(ButtonFrame, text="Reset Game", font=('Times 26 bold'), height=3, width=15, bg='gainsboro', command=reset_game)
buttonReset.grid(row=1, column=0, sticky=E+W)

button1=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro' , command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)
button2=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)
button3=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)
button5=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)
button6=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)
button8=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)
button9=Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

lbltitle=Label(TitleFrame, font=('arial',20,'bold'), text="Tic Toc", bd=7)
lbltitle.pack()
lblPTurn=Label(GameFrame, font=('arial',40,'bold'), text="Whose Turn : ", padx=2,pady=2)
lblPTurn.grid(row=2, column=0, sticky=W)
txtTurn=Entry(GameFrame, font=('arial',40,'bold'), bd=2, fg="black" , textvariable= PlayerTurn, width=10, justify=LEFT)
txtTurn.grid(row=2, column =1 )

lblPTurn=Label(MainWindows, font=('arial',10,'bold'), text="marciniakjakub93@gmail.com ", padx=2,pady=2)
lblPTurn.grid(row=5, column=0, sticky=W)

root.mainloop()
