import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import by
from selenium.webdriver.common.by import by


s=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element("css selector","input.search-keyword").send_keys("ber")
time.sleep(4)
#count= len(driver.find_element_by_xpath("//div[@class='products']/div"))
#assert count==3
button= driver.find_element_by_xpath("//div[@class='product-action']/button").click()
#b=driver.find_element_by_xpath("//div[@class='product-action']/button")
print("hiiiiiii:" ,button)
#for buttons in button:
     # buttons.click()


driver.find_element_by_css_selector("img[alt='Cart']").click()
###driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']/").click()
##hello