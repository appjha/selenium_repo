from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import by
from selenium.webdriver.support.select import Select

s=Service("C:\\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element("name","name").send_keys("aparna")
driver.find_element("name","email").send_keys("aparna@gmail.com")
#driver.find_element_by_name("name").send_keys("aparna")
#driver.find_element_by_css_selector("input[name='name']").send_keys("baiju")
#driver.find_element_by_name("email").send_keys("baiju@gmail.com")
#driver.find_element_by_name()
#driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_xpath("//input[@type='submit']").click()
dropdown=Select(driver.find_element("id","exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
driver.find_element("id","exampleCheck1").click()
driver.find_element("xpath","//input[@type='submit']").click()
print(driver.find_element("class name"," alert-success ").text)
