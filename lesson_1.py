from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as CS

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(service=CS(ChromeDriverManager().install()), options=chrome_options)
browser.get('http://suninjuly.github.io/explicit_wait2.html')
try:
    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_btn = browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.ID, 'input_value').text
    x = calc(x_element)
    input1 = browser.find_element(By.ID, 'answer').send_keys(x)
    submit_btn = browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()

