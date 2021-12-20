import XlUtility
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.maximize_window()

path = r"C:\Users\91638\OneDrive\Desktop\New Microsoft Excel Worksheet.xlsx"

row = XlUtility.GetRowCount(path, "Sheet1")

for r in range (2,row+1):
    username = XlUtility.ReadData(path, "Sheet1", r, 1)
    password = XlUtility.ReadData(path, "Sheet1", r, 2)

    browser.find_element(By.ID,"txtUsername").send_keys(username)
    browser.find_element(By.ID,"txtPassword").send_keys(password)
    browser.find_element(By.ID,"btnLogin").click()

    try:
        browser.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
        print("Success")
        XlUtility.WriteData(path, "Sheet1", r, 3, "Passed")
        souceDrop = browser.find_element(By.ID,"welcome")
        select = Select(souceDrop)
        select.select_by_index(3)
        browser.find_element(By.XPATH,"//*[@id='welcome-menu']/ul/li[3]/a").click()
    except:
        continue
