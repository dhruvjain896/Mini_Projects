from bs4 import BeautifulSoup
import lxml
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developement\chromedriver.exe" # Enter your executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSdvj-g1Mpx1KdBx8K2gJdmpdnONk5P8G1jnNvm5jqylFGcqfw/viewform?usp=sf_link'
# Make your own google form so that you can create the spreadsheet in your google account
zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
# Filter searches according to your need on the zillow website manually and then paste the url here in zillow_url field
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
accept_language = "en-US,en;q=0.9"

response = requests.get(zillow_url, headers={"User-Agent": user_agent, "Accept-Language": accept_language})
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, 'lxml')

prices = []
links = []
addresses = []

product_prices = soup.find_all(class_='list-card-price')
for product in product_prices:
    prices.append(product.getText()[:6])

product_addresses = soup.find_all(class_='list-card-link')
for product in product_addresses:
    if product.getText() != '':
        addresses.append(product.getText())
        links.append(product.get('href'))

for i in range(0, len(prices)):
    driver.get(google_form)
    time.sleep(5)
    property_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    property_address.send_keys(addresses[i])
    property_price.send_keys(prices[i])
    property_link.send_keys(links[i])

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(5)
