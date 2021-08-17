from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class checkfile1():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")


    def check1(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def check2(self):
       self.driver.find_element_by_id("laptopsImg").click()
       text=self.driver.find_element_by_css_selector('[class="select  ng-binding"]').text
       return text

    def showtext(self):
        text1=self.driver.find_element_by_css_selector('[class="roboto-bold ng-binding"]').text
        return text1
