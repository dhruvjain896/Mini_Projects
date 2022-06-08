from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 50 # Enter your promised download speed
PROMISED_UP = 10  # Enter your promised up speed
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL_ID"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = "C:\Developement\chromedriver.exe" # Enter your executable path
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(120)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        input_email = self.driver.find_element_by_name('text')
        input_email.send_keys(TWITTER_EMAIL)
        next = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span')
        next.click()
        time.sleep(5)
        try:
            username = self.driver.find_element_by_name('text')
            username.send_keys('ENTER_YOUR_TWITTER_USERNAME')
            username.send_keys(Keys.ENTER)
            time.sleep(5)
        except NoSuchElementException:
            pass
        input_password = self.driver.find_element_by_name('password')
        input_password.send_keys(TWITTER_PASSWORD)
        log_in_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in_button.click()
        try:
            correct_email = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/span/span')
            correct_email.click()
        except NoSuchElementException:
            pass
        time.sleep(5)
        tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}mbps down/{self.up}mbps up when I pay for {PROMISED_DOWN}mbps down/{PROMISED_UP}mbps up?"
        tweet_input.send_keys(tweet)
        time.sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
