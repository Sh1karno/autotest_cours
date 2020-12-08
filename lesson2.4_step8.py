from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import *

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)

    button_book = browser.find_element_by_id("book")

    price_element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button_book.click()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)

    y = str(log(abs(12 * sin(x))))

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    submit_button_element = browser.find_element_by_id("solve")
    sleep(1)
    submit_button_element.click()

    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[-1])
    sleep(1)
    browser.switch_to.alert.accept()
    sleep(1)

    browser.quit()

finally:
    sleep(15)
    browser.quit()
