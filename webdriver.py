from selenium import webdriver


from selenium.webdriver.chrome.service import Service
s=Service("C:\\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()

