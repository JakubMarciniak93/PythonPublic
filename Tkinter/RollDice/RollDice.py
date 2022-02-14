import tkinter as tk
import random

root = tk.Tk()
root.geometry('400x400')
root.configure(background="green")
root.title('RollDice')

label =tk.Label(root, text= "", font=('arial', 200))
def roll_dice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    print(f'{random.choice(dice)}{random.choice(dice)}')
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button=tk.Button(root,text='ROLL DICE',background="lightgreen", width=40,height=5, command=roll_dice)
button.pack()

root.mainloop()

