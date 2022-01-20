import requests
from twilio.rest import Client
import os

# Enter your required stock name
STOCK_NAME = "TSLA"
# Enter your required stock's company name
COMPANY_NAME = "Tesla Inc"

# Enter your Alpha Vantage API Key for Stock price alert
Alpha_Vantage_API_Key = os.environ.get("YOUR_ALPHA_VANTAGE_API_KEY")

# Get your News API KEY from https://newsapi.org/
News_API_Key = os.environ.get("YOUR_NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
mobile_number = os.environ.get("MY_MOBILE_NUMBER")
twilio_mobile_number = os.environ.get("TWILIO_MOBILE_NUMBER")
twilio_whatsapp_number = os.getenv('YOUR_TWILIO_WHATSAPP_NUMBER')

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": Alpha_Vantage_API_Key,
    "outputsize": "compact",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
daily_closing_price = [float(value["4. close"]) for (key, value) in stock_data.items()][:2]
percent_diff = (daily_closing_price[0] - daily_closing_price[1]) / daily_closing_price[0] * 100
abs_percent_diff = abs(percent_diff)

up_or_down = '🔺' if percent_diff > 0 else '🔻'

news_params = {
    "apiKey": News_API_Key,
    "qInTitle": COMPANY_NAME,
}

if abs_percent_diff >= 1:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    top_3_articles = news_data['articles'][:3]

    client = Client(account_sid, auth_token)

    for i in range(0, 3):
        news_message = f"{STOCK_NAME}: {up_or_down}{round(abs_percent_diff)}%\nHeadline: {top_3_articles[i]['title']}\nBrief: {top_3_articles[i]['description']}"
        message = client.messages \
            .create(
            body=news_message,
            from_=f"{twilio_mobile_number}",
            # from_="whatsapp:{twilio_whatsapp_number}",
            to=f"{mobile_number}",
            # to=f"whatsapp:{mobile_number}"
        )
        print(message.status)
