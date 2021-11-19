import smtplib
import datetime as dt
import random
import pandas as pd

today_date = dt.datetime.now().day
today_month = dt.datetime.now().month
today = (today_month, today_date)

my_email = "someone@gmail.com"
password = "password"

df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        letter = file.read()
    birthday_person = birthdays_dict[today]
    letter = letter.replace("[NAME]", f"{birthday_person['name']}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )
