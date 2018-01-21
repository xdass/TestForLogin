import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.get('https://ru.investing.com/')
driver.find_element_by_xpath('//a[normalize-space(.)="Зарегистрироваться"]').click()

el = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#signUPBtn'))
)
el.click()
# time.sleep(5)
# el = driver.find_element_by_css_selector('#signup #signUPBtn')
# el.click()