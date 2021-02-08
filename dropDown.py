from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import by

s=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements("xpath","//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option1":
      checkbox.click()
      assert checkbox.is_selected()


radiobutton = driver.find_element("name","radioButton")
radiobutton.click()
assert radiobutton[2].is_selected()



