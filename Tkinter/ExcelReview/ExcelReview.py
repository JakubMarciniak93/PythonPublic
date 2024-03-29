from tkinter import *
import customtkinter
import numpy
import pandas as pd
from tkinter import ttk, filedialog, messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Excel Review")
root.geometry("900x400")

def open_excel():
    my_file = filedialog.askopenfilename(title="Open File",
        filetype=(("Excel Files", ".xl**"),("All Files", "*.*")))
    try:
        #dataframe
        df = pd.read_excel(my_file)
        #print(df)
        #print("test")
    except Exception as e:
        messagebox.showerror("Problem!", f"There was a problem {e}")

    #Clear the treeview
    my_tree.delete(*my_tree.get_children())
    #Headers
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    #show the headers
    for col in my_tree['column']:
        my_tree.heading(col, text=col)
    #show data
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("","end", values=row)
        

#Treeview
my_tree = ttk.Treeview(root)
my_tree.pack(pady=20)

#tree style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
    background="grey",
    foreground="black",
    rowhaight=25,
    filedbackground='#707070')
#color  selected
style.map('Treeview', background=[('selected', "#535353")])

#Button
my_button = customtkinter.CTkButton(root, text="Open File", command=open_excel)
my_button.pack(pady=20)


root.mainloop()