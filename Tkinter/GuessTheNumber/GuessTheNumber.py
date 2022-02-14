import tkinter as tk
import random

#Generate number
random_number = random.randrange(11)
print(random_number)
x=0
#find function
def find_a_number():
    global x
    x += 1
    textDisplay.delete("1.0", "end")
    try:
        m = int(input_text.get())
    except ValueError:
        textDisplay.insert(tk.END, "Musisz wprowadzić wartość liczby całkowitej.")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))

    if m < 0:
        textDisplay.insert(tk.END, "Wprowadziłeś wartość ujemną. Musisz wpisać conajmniej 0")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))
    elif m >10:
        textDisplay.insert(tk.END, "Wprowadziłeś wartość większą od 10.")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))
    elif m > random_number:
        textDisplay.insert(tk.END, "Za duża liczba")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))
    elif m < random_number:
        textDisplay.insert(tk.END, "Za mała liczba")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))
    else:
        textDisplay.insert(tk.END, "Udało się!")
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Ilość prób: " + str(x)))
        textDisplay.insert(tk.END, '\n\n')
        textDisplay.insert(tk.END, str("Wygenerowano nową liczbę"))


################################MAIN WINDOW####################
root = tk.Tk()
root.geometry('550x300')
root.configure(background="green")
root.title('Guess The Number')
input_text=tk.StringVar()
label_info = tk.Label(root, text= "Wprowadź Liczbę Całkowitą od 0 do 10 ", font=('arial', 20))
label_info.pack()
number_entry = tk.Entry(root, textvariable=input_text, justify='center')
number_entry.pack()
button_number = tk.Button(root,text= "Sprawdz liczbę", command=find_a_number)
button_number.pack()
textDisplay = tk.Text(root, width=30, height= 5, bd=16, font=('arial',20,'bold'))
textDisplay.pack()
button_reset = tk.Button(root,text= "Reset")
button_reset.pack()
#######################################################

root.mainloop()