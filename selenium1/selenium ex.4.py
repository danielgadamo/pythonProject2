from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_css_selector('[name="userName"]').send_keys('tutorial')
driver.find_element_by_css_selector('[type="password"]').send_keys('tutorial')
driver.find_element_by_css_selector('[type="submit"]').click()

sleep(3)





driver.find_element_by_css_selector('[href="reservation.php"]').click()
driver.find_element_by_css_selector('[value="oneway"]').click()
driver.find_element_by_css_selector('[value="First"]').click()

# departing=driver.find_element_by_css_selector('[name="fromPort"]')
# selectdeparting=Select(departing)
# selectdeparting.select_by_value("New York")
# sleep(3)
# month=driver.find_element_by_name('name="fromMonth"')
# selectmonth=Select(month)
# selectmonth.select_by_value("4")








driver.find_element_by_css_selector('[name="findFlights"]').click()
sleep(5)

driver.close()