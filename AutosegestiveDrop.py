import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import by

s=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.find_element("id","autosuggest").send_keys("ind"))
time.sleep(2)
countries=driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("countries")
print(len(countries))
for country in countries:
   if country.text=="India":
       country.click()
       break

