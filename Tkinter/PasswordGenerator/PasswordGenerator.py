from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("900x300")

my_password = chr(randint(30,126))

def new_rand():
    pas_entry.delete(0, END)
    pas_length = int(my_entry.get())
    my_password = ''
    for x in range(pas_length):
        my_password += chr(randint(33,126))

    pas_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pas_entry.get())


#Frame
mainFrame = LabelFrame(root, text="How many characters?")
mainFrame.pack(pady=20)
#entry
my_entry = Entry(mainFrame, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)
pas_entry = Entry(root, text='', font=("Helvetica",30), bd=0, bg='systembuttonface')
pas_entry.pack(pady=20)
#button Frame
button_frame= Frame(root)
button_frame.pack(pady=20)
my_button = Button(button_frame, text='Generate', command=new_rand)
my_button.grid(row=0, column=0, padx=10)
clip_button = Button(button_frame, text='Copy Output', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
