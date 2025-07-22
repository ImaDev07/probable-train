# 4. Selenium

# 1. Вопрос
#Selenium- это инструмент для автоматизации веб-браузеров

# 2. Вопрос
# WebDriver — управление браузером
#Поиск: по ID, CSS, XPath
#Клик: click()
# Ввод: send_keys()
#Ожидания: implicit (implicitly_wait()), explicit (WebDriverWait())



# Практика
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python Selenium')
search_box.send_keys(Keys.RETURN)

time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, 'h3')[:3]
for index, result in enumerate(results, 1):
    print(f'Вывод: {index}: {result.text}')

driver.quit()

#Selenium