from selenium import webdriver
import os
import time
from password import UserName,Password
driver = webdriver.Firefox(executable_path=r'D:\Dars\Doran Course\Python_Basics\geckodriver.exe')

driver.get(r'http://onlineb.douran.academy/python-engineering/')

blog = driver.find_element_by_xpath(r'//*[@id="name"]')
blog.send_keys("mhaddad206@gmaail.com")

blog = blog.find_element_by_xpath(r'//*[@id="pwd"]')
blog.send_keys("123456")

blog = blog.find_element_by_xpath(r'//*[@id="login-button"]')
blog.click()


