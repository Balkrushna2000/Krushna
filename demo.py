from selenium.webdriver.chrome.service import Service
from selenium import webdriver


#chrome driver
service_obj= Service("B:\Python\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)


# Microsft edge browser driver
'''service_obj= Service("B:\Python\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)'''


# firef0x  browser driver

'''service_obj=Service("B:\Python\geckodriver-v0.32.0-win-aarch64\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)'''
driver.get("https://www.facebook.com/login/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/")
driver.refresh()
driver.back()
driver.forward()
driver.minimize_window()
driver.close()