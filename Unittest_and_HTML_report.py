import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginHRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
        cls.browser.maximize_window()

    def test_pagetitle(self):
        self.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.assertEqual("OrangeHRM", self.browser.title,"Webpage titles are not same")

    def test_login(self):
        self.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.browser.find_element(By.ID, "btnLogin").click()
        self.assertEqual("OrangeHRM",self.browser.title,"Webpage title are not same")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        print("Tests are completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\91638\PycharmProjects\Selenium_with_python\Reports"))