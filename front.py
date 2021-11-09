from tkinter import *
from tkinter import messagebox, simpledialog
import back
import random
import password_generator
from datetime import datetime
import os

window = Tk()
pic = PhotoImage(file="scaled_gta5_police_logo.png")
label2 = Label(window, image=pic).grid(row=0, column=4, rowspan=7, columnspan=5)


def check_fields():
    rights = 0
    if Complainant_Name_text.get() != "" and Father_Mother_Name_text.get() != "" and Complainant_Address_text.get() != "" and Complainant_email_ID_text.get() != "" and Place_of_incident_text.get() != "" and Date_of_incident_text.get() != "" and Time_of_the_incident_text.get() != "" and Description_of_the_incident_text.get() != "":
        rights += 1
    else:
        messagebox.showerror("Error", "All fields are mandatory")

    if len(str(Complainant_Mobile_number_text.get())) == 10:
        rights += 1
    else:
        messagebox.showerror("Error", "Please enter a valid Phone Number")

    if '@' in Complainant_email_ID_text.get() and '.com' in Complainant_email_ID_text.get():
        rights += 1
    else:
        messagebox.showerror("Error", "Please enter a valid email address")

    try:
        datetime.strptime(Date_of_incident_text.get(), '%d/%m/%Y')
        rights += 1
    except:
        messagebox.showerror("Error", "Please enter a valid date")

    try:
        datetime.strptime(Time_of_the_incident_text.get(), '%H:%M')
        rights += 1
    except:
        messagebox.showerror("Error", "Please enter a valid time")

    if rights == 5:
        return True
    return False


def lodge_command():
    if check_fields():
        user_id = random.randint(000000, 999999)
        while user_id in back.users:
            user_id = random.randint(000000, 999999)

        back.users.append(user_id)

        password = password_generator.generate_password()

        messagebox.showinfo("Information",
                            f"Please Note Your Credentials:-\n\nUser ID: {user_id}\nPassword: {password}")

        back.insert(user_id, password, Complainant_Name_text.get(), Father_Mother_Name_text.get(),
                    Complainant_Address_text.get(),
                    Complainant_Mobile_number_text.get(), Complainant_email_ID_text.get(),
                    Place_of_incident_text.get(), Date_of_incident_text.get(), Time_of_the_incident_text.get(),
                    Description_of_the_incident_text.get())


def user_info():
    user_id_answer = simpledialog.askstring("User Id", "Enter your user id", parent=window)
    password_answer = simpledialog.askstring("Password", "Enter your password", parent=window)
    return user_id_answer, password_answer


def view_command():
    answers = user_info()
    user_id_answer = answers[0]
    password_answer = answers[1]
    try:
        info = back.view(user_id_answer, password_answer)[0]
        messagebox.showinfo("Information",
                            f"Here is your lodged FIR:-\n\nUser ID: Complainant’s Name: {info[2]}\nFather"
                            f"’s/Mother’s Name: {info[3]}\nComplainant’s Address: {info[4]}\nComplainant’s "
                            f"Mobile number: {info[5]}\nComplainant’s email ID: {info[6]}\nPlace where the "
                            f"incident took place: {info[7]}\nDate of incident: {info[8]}\nTime of the "
                            f"incident: {info[9]}\nDescription of the incident: \n{info[10]}")
    except:
        messagebox.showerror("Error", "Please enter valid User ID or Password")


def update_fir():
    answers = user_info()
    user_id_answer = answers[0]
    password_answer = answers[1]
    try:
        info = back.view(user_id_answer, password_answer)[0]
        Complainant_Name_text.set(info[2])
        Father_Mother_Name_text.set(info[3])
        Complainant_Address_text.set(info[4])
        Complainant_Mobile_number_text.set(info[5])
        Complainant_email_ID_text.set(info[6])
        Place_of_incident_text.set(info[7])
        Date_of_incident_text.set(info[8])
        Time_of_the_incident_text.set(info[9])
        Description_of_the_incident_text.set(info[10])

        def update_command():
            if check_fields():
                back.update(user_id_answer, password_answer, Complainant_Name_text.get(), Father_Mother_Name_text.get(),
                            Complainant_Address_text.get(),
                            Complainant_Mobile_number_text.get(), Complainant_email_ID_text.get(),
                            Place_of_incident_text.get(), Date_of_incident_text.get(), Time_of_the_incident_text.get(),
                            Description_of_the_incident_text.get())
                window.destroy()
                os.system('front.py')

        update_button = Button(window, text="UPDATE", width=12, command=update_command)
        update_button.grid(row=8, column=2)
        update_button.pack_forget()
    except:
        messagebox.showerror("Error", "Please enter valid User ID or Password")


def delete_command():
    answers = user_info()
    user_id_answer = answers[0]
    password_answer = answers[1]
    try:
        info = back.view(user_id_answer, password_answer)[0]
        back.delete(user_id_answer, password_answer)
    except:
        messagebox.showerror("Error", "Please enter valid User ID or Password")


window.wm_title("Lodge Your FIR")

l1 = Label(window, text="Complainant’s Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Father’s/Mother’s Name")
l2.grid(row=0, column=2)

l3 = Label(window, text="Complainant’s Address")
l3.grid(row=1, column=0)

l4 = Label(window, text="Complainant’s Mobile number")
l4.grid(row=1, column=2)

l5 = Label(window, text="Complainant’s email ID")
l5.grid(row=2, column=0)

l6 = Label(window, text="Place where the incident took place")
l6.grid(row=2, column=2)

l7 = Label(window, text="Date of incident (01/01/0001)")
l7.grid(row=3, column=0)

l8 = Label(window, text="Time of the incident (00:00)")
l8.grid(row=3, column=2)

l9 = Label(window, text="Description of the incident")
l9.grid(row=4, column=0)

Complainant_Name_text = StringVar()
e1 = Entry(window, textvariable=Complainant_Name_text)
e1.grid(row=0, column=1)

Father_Mother_Name_text = StringVar()
e2 = Entry(window, textvariable=Father_Mother_Name_text)
e2.grid(row=0, column=3)

Complainant_Address_text = StringVar()
e3 = Entry(window, textvariable=Complainant_Address_text)
e3.grid(row=1, column=1)

Complainant_Mobile_number_text = IntVar()
e4 = Entry(window, textvariable=Complainant_Mobile_number_text)
e4.grid(row=1, column=3)

Complainant_email_ID_text = StringVar()
e5 = Entry(window, textvariable=Complainant_email_ID_text)
e5.grid(row=2, column=1)

Place_of_incident_text = StringVar()
e6 = Entry(window, textvariable=Place_of_incident_text)
e6.grid(row=2, column=3)

Date_of_incident_text = StringVar()
e7 = Entry(window, textvariable=Date_of_incident_text)
e7.grid(row=3, column=1)

Time_of_the_incident_text = StringVar()
e8 = Entry(window, textvariable=Time_of_the_incident_text)
e8.grid(row=3, column=3)

Description_of_the_incident_text = StringVar()
e9 = Entry(window, textvariable=Description_of_the_incident_text)
e9.grid(row=5, column=0)

b1 = Button(window, text="Lodge FIR", width=12, command=lodge_command)
b1.grid(row=7, column=0, padx=15, pady=15)

b2 = Button(window, text="View FIR", width=12, command=view_command)
b2.grid(row=7, column=1, padx=15, pady=15)

b3 = Button(window, text="Update FIR", width=12, command=update_fir)
b3.grid(row=7, column=2, padx=15, pady=15)

b4 = Button(window, text="Withdraw FIR", width=12, command=delete_command)
b4.grid(row=7, column=3, padx=15, pady=15)

b7 = Button(window, text="Close", width=12, command=window.destroy)
b7.grid(row=7, column=4, padx=15, pady=15)

window.mainloop()
