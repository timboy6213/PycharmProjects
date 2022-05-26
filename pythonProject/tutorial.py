from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)
# driver.find_element_by_class_name("sc-e6ba31f5-3").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-d6aee74c-1"))
)
titles = driver.find_elements_by_class_name("sc-b205d8ae-3")
for title in titles:
    print(title.text)

link = driver.find_element_by_link_text("比特幣")
link.click()

time.sleep(5)
driver.quit()
