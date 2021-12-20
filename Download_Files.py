from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ChromeOption = Options()
ChromeOption.add_experimental_option("prefs",{"download.default_directory" : "D:\Vidmore"})
browser = webdriver.Chrome(executable_path="C:\Users\91638\chromedriver.exe",options=ChromeOption)
browser.get("http://demo.automationtesting.in/FileDownload.html")
browser.maximize_window()

browser.find_element(By.ID,"textbox").send_keys("Test the testing file sending option")
browser.find_element(By.ID,"createTxt").click()
browser.find_element(By.ID,"link-to-download").click()

browser.find_element(By.ID,"pdfbox").send_keys("Test the testing file sending option")
browser.find_element(By.ID,"createPdf").click()
browser.find_element(By.ID,"pdf-link-to-download").click()
