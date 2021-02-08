from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import by

s=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element("css selector","#username").send_keys("ap")
driver.find_element("css selector",".password").send_keys("appppp")
driver.find_element("css selector",".password").clear()

#driver.find_element("css selector","#Login").click()
#driver.find_element("css selector","#rememberUn").click()
driver.find_element("partial link text","Forgot Your Password?").click()
driver.find_element("xpath","//a[text()='Cancel']").click()
#print(driver.find_element("xpath","//form[@name='login']/div[1]/label").text)
#print(driver.find_element("css selector","form[name='login']label:nth-child(3)").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element("class name",".label").text)