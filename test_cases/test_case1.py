from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from home.py import click_downloads_button

service = Service(r'C:\selenium_testing\chromedriver.exe')  


driver = webdriver.Chrome(service=service)


driver.get("https://www.python.org")

driver = click_downloads_button(driver)

print(driver.title)


search_bar = driver.find_element(By.NAME, "q")

search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN) 


print(driver.current_url)

input (10)


driver.quit()
