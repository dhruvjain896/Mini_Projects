from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developement\chromedriver.exe" #Enter your executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

email = "YOUR_EMAIL_ID"
password = "YOUR_PASSWORD"

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105080838&keywords=python%20developer&location=New%20York%2C%20United%20States") #You can enter your job serach filter url
time.sleep(5)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(5)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
