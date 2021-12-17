from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://www.expedia.com/")
browser.implicitly_wait(10)
print("Title of the page:",browser.title)
print("URL of the page:", browser.current_url)
browser.quit()