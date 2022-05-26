#爬取IG照片
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import time
path = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

username =WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password =WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()
username.send_keys('0926919269')
password.send_keys('mory03020411')
login.click()

search =WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
keyword = "#cat"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
)
for i in range(5):
    driver.execute_script("window.scroll(0,document.body.scrollHeight);")
    time.sleep(3)
imgs = driver.find_elements_by_class_name('FFVAD')

path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword+str(count)+'jpg')
    #print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count +=1