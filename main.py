from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = "C:\Developement\chromedriver.exe" #Enter your executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

phone_no = "YOUR_TINDER_NUMBER"
# You have to enter OTP manually while logging is going on.

driver.get("https://tinder.com/")
time.sleep(10)
i_accept = driver.find_element_by_xpath('//*[@id="c1276625974"]/div/div[2]/div/div/div[1]/button/span')
i_accept.click()

log_in = driver.find_element_by_xpath('//*[@id="c1276625974"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
time.sleep(10)

try:
    log_in_with_phone_number = driver.find_element_by_xpath(
        '//*[@id="c1497966410"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]')
    log_in_with_phone_number.click()

except NoSuchElementException:
    more_options = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    log_in_with_phone_number = driver.find_element_by_xpath(
        '//*[@id="c1497966410"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]')
    log_in_with_phone_number.click()

time.sleep(20)
input_phone_no = driver.find_element_by_name('phone_number')
input_phone_no.send_keys(phone_no)
time.sleep(10)
continue_button = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div[1]/button/span')
continue_button.click()
time.sleep(30)
another_continue_button = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div[1]/button')
another_continue_button.click()
time.sleep(10)
send_email = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div[1]/div[2]/button')
send_email.click()
time.sleep(30)
confirm_email = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div[1]/button')
confirm_email.click()
time.sleep(10)
allow_button = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div/div/div[3]/button[1]/span')
allow_button.click()
time.sleep(5)
not_interested = driver.find_element_by_xpath('//*[@id="c1497966410"]/div/div/div/div/div[3]/button[2]/span')
not_interested.click()
time.sleep(20)

for n in range(10):
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
