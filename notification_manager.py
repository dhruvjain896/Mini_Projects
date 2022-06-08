from twilio.rest import Client
import smtplib
import requests

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_ACCOUNT_AUTH_TOKEN"
mobile_number = "YOUR_MOBILE_NUMBER"
twilio_mobile_number = "YOUR_TWILIO_MOBILE_NUMBER"

my_email = "YOUR_EMAIL_ID"
password = "YOUR_EMAIL_ID_PASSWORD"

Sheety_API = "YOUR_SHEETY_API"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_whatsapp(self, message):
        message = self.client.messages.create(
            body=message,
            # from_=f"{twilio_mobile_number}",
            from_="whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER",
            # to=f"{mobile_number}",
            to=f"whatsapp:{mobile_number}"
        )

    def send_email(self, message):
        response = requests.get(Sheety_API)
        data = response.json()["users"]

        for user in data:
            user_email = user["email"]
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=user_email,
                    msg=f"Subject:LOW PRICE ALERT!\n\n{message}"
                )
