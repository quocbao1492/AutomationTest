from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://tinhte.vn")
driver.find_element_by_xpath("//*[@id='navigation']/div/div/div/nav/div/div/ul[2]/li[1]/a").click()
time.sleep(4)

driver.quit()