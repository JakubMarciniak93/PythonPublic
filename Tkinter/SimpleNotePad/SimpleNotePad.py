import tkinter as tk
from tkinter import filedialog as fd

SimpleNotepad = tk.Tk()
SimpleNotepad.geometry("700x500")
SimpleNotepad.configure(background="green")
SimpleNotepad.title("Simple Notepad")

def open_file():
    filename = fd.askopenfilename(filetypes=[("file", "*.*")])
    if filename:
        with open(filename, "r", -1, "utf-8") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    filename = fd.asksaveasfilename(filetypes=[("file", "*.txt")],defaultextension="*.txt")
    if filename:
        with open(filename, "w", -1, "utf-8") as file:
            file.write(text.get(1.0, tk.END))

        #create menu picklist
menu = tk.Menu(SimpleNotepad)
submenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=open_file)
submenu.add_command(label="Save", command=save_file)
SimpleNotepad.config(menu=menu, width=50, height=30)
#create text place + scroll
text = tk.Text(SimpleNotepad)
sb_text = tk.Scrollbar(SimpleNotepad)
sb_text.place(in_=text, relx=1., rely=0, relheight=1.)
sb_text.config(command=text.yview)
labelinfo=tk.Label(SimpleNotepad,text="If you want open or save file use File menu")
labelinfo.grid(row=0,column=1)
text.config(yscrollcommand=sb_text.set)
#text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)
text.grid(row=1,column=1)

SimpleNotepad.mainloop()

