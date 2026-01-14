from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.scraperapi.com/web-scraping/selenium/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")