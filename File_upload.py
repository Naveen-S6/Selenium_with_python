from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("http://testautomationpractice.blogspot.com/")
browser.maximize_window()
browser.switch_to.frame(0)
browser.find_element(By.ID,"RESULT_FileUpload-10").send_keys(r"C:\Users\91638\Downloads\drew-beamer-Vc1pJfvoQvY-unsplash.jpg")
