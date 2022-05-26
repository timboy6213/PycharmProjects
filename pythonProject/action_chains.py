# 自動完網頁遊戲
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

path = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://tsj.tw/")

blow = driver.find_element_by_id("click")
blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
items = [driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'),
         driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'),
         driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i')]
prices = [driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'),
          driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'),
          driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]')]

print(blow_count.text)
actions = ActionChains(driver)
actions.click(blow)

for i in range(10000):
    actions.perform()
    count = int(blow_count.text.replace("您目前擁有", "").replace("技術點", ""))
    for j in range(3):
        price = int(prices[j].text.replace("技術點", ""))
        if price <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(items[j])
            upgrade_action.click()
            upgrade_action.perform()
            break
# time.sleep(3)
# driver.quit()
