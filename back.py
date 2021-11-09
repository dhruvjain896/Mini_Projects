import sqlite3

users = []


def connect():
    connection = sqlite3.connect("fir.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS fir_record( user_id int PRIMARY KEY,Password text,Complainant_Name_text text,"
        "Father_Mother_Name_text text,Complainant_Address_text text,Complainant_Mobile_number_text int,"
        "Complainant_email_ID_text text,Place_of_incident_text text,Date_of_incident_text text,"
        "Time_of_the_incident_text text, Description_of_the_incident_text text)")
    connection.commit()
    connection.close()


def insert(user_id, Password, Complainant_Name_text, Father_Mother_Name_text, Complainant_Address_text,
           Complainant_Mobile_number_text, Complainant_email_ID_text, Place_of_incident_text, Date_of_incident_text,
           Time_of_the_incident_text, Description_of_the_incident_text):
    connection = sqlite3.connect("fir.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO fir_record VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, Password, Complainant_Name_text, Father_Mother_Name_text, Complainant_Address_text,
                 Complainant_Mobile_number_text, Complainant_email_ID_text, Place_of_incident_text,
                 Date_of_incident_text, Time_of_the_incident_text, Description_of_the_incident_text))
    connection.commit()
    connection.close()


def view(user_id=000000, Password=""):
    connection = sqlite3.connect("fir.db")
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM fir_record WHERE user_id=? AND Password=? ",
        (user_id, Password))
    rows = cur.fetchall()
    connection.close()
    return rows


def delete(user_id, Password):
    connection = sqlite3.connect("fir.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM fir_record WHERE user_id=? AND Password=?", (user_id, Password))
    connection.commit()
    connection.close()


def update(user_id, Password, Complainant_Name_text, Father_Mother_Name_text, Complainant_Address_text,
           Complainant_Mobile_number_text, Complainant_email_ID_text, Place_of_incident_text, Date_of_incident_text,
           Time_of_the_incident_text, Description_of_the_incident_text):
    connection = sqlite3.connect("fir.db")
    cur = connection.cursor()
    cur.execute("UPDATE fir_record SET Complainant_Name_text = ?, Father_Mother_Name_text = ?, "
                "Complainant_Address_text = ?, Complainant_Mobile_number_text = ?, Complainant_email_ID_text = ?, "
                "Place_of_incident_text = ?, Date_of_incident_text = ?, Time_of_the_incident_text = ?, "
                "Description_of_the_incident_text = ? WHERE user_id = ? AND Password = ?",
                (Complainant_Name_text, Father_Mother_Name_text, Complainant_Address_text,
                 Complainant_Mobile_number_text, Complainant_email_ID_text, Place_of_incident_text,
                 Date_of_incident_text, Time_of_the_incident_text, Description_of_the_incident_text, int(user_id), Password))
    connection.commit()
    connection.close()


connect()
