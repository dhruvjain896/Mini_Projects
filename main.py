from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    label3.config(text=str(round(float(entry.get())*1.60934, 2)))


entry = Entry(width=10)
entry.insert(END, string='0')
entry.grid(row=0, column=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

window.mainloop()
