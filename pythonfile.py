from tkinter import *

from PIL import ImageTk, Image


def click():
    text_entry = textentry.get()
    if int(text_entry) and len(text_entry) == 10:
        print("Login Approved")
        root.destroy()
        import os
        os.system('front.py')
    else:
        print("Access Denied")
        label1 = Label(bottomFrame, text="Invalid Number. Try again", fg="black", bg="red")
        label1.grid(row=1, column=1)


root = Tk()
root.title("Login Window")
root.geometry("620x520+100+00")
root.configure(background="dark blue")

topFrame = Frame(root, bg="light blue")
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
photo = ImageTk.PhotoImage(Image.open(r"scaled_lspd_logo.jpg"))
Label(topFrame, image=photo).grid(row=1, column=1, sticky=W)
label = Label(topFrame, text="ONLINE \n FIR \n SYSTEM ", fg="black", bg="light blue", font=(None, 25)).grid(
    row=1, column=3, sticky=E)

Label(topFrame, text="Enter Number", fg="black", bg="light blue", font=(None, 15)).grid(row=4, column=3)
textentry = Entry(topFrame, width=30, fg="black", bg="white", show="*")
textentry.grid(row=5, column=3, sticky=W)
Button(topFrame, text="Submit", width=10, command=click).grid(row=6, column=3, sticky=W)


def close():
    exit()


Label(bottomFrame,
      text="NOTE: This is the official System Application of Department of Police, Los Santos, United States.\n"
           "Content on this app is published and 'managed' by Los Santos Police, United States.\n"
           "For any query regarding this website, Please contact the 'App Administrator.'",
      fg="red", bg="white").grid(row=6, column=1, sticky=W)
Button(bottomFrame, text="Click to Exit", width=10, command=close).grid(row=7, column=1, sticky=S)

root.mainloop()
