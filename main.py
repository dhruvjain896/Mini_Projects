from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

product_url = "https://www.amazon.in/Samsung-Convection-Microwave-CE1041DSB2-TL/dp/B01LF9EX1G/ref=sr_1_3?crid=3IOKG6NUE9THZ&th=1" #Enter your product URL(Only Amazon)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
accept_language = "en-US,en;q=0.9"
my_email = "YOUR_EMAIL_ID_FROM_WHICH_YOU_WANT_TO_SEND_NOTIFICATION"
password = "YOUR_EMAIL_ID_PASSWORD"
my_price = 5000 #Type the lowest price at which you want to recieve notification for the product

response = requests.get(product_url, headers={"User-Agent": user_agent, "Accept-Language": accept_language})
product_webpage = response.text
soup = BeautifulSoup(product_webpage, 'lxml')
product_price_unformatted = soup.find(name="span", class_="priceBlockBuyingPriceString").getText()
product_price = float(''.join(product_price_unformatted[1:].split(',')))
product_title = soup.find(name="span", class_="product-title-word-break").getText()
product_title = product_title.strip(" ")


if product_price <= my_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="EMAIL_ID_ON_WHICH_YOU_WANT_TO_RECIEVE_NOTIFICATION",
            msg=f"Subject:Amazon Price Alert!\n\n{product_title} now Rs {product_price_unformatted[1:]}\n{product_url}"
        )
