from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

EMAIL = 'ENTER_YOUR_EMAIL_ID'
PASSWORD = 'ENTER_YOUR_PASSWORD'
SIMILAR_ACCOUNT = 'linustech' #Enter username of the personality account whose followers you want to follow


class InstaFollower:
    def __init__(self):
        chrome_driver_path = "C:\Developement\chromedriver.exe" # Enter your executable path
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys(EMAIL)
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(10)
        try:
            not_now_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            not_now_button.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(10)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_account_list = self.driver.find_elements_by_class_name('Pkbci')
        for account in follow_account_list:
            try:
                account.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
