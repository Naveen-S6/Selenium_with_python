from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://www.amazon.in/")
browser.maximize_window()

cookies = browser.get_cookies()
print(len(cookies))
print(cookies)

cookie = {"value":"1223423","name":"Naveen"}
browser.add_cookie(cookie)
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)

browser.delete_cookie("Naveen")
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)

browser.delete_all_cookies()
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)
browser.quit()