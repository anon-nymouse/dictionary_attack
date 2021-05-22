import sys
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


user = ['admin@admin.com']
psw = [s for s in range(15,50)]
psw2 = [a for a in range(50,60)]
psw.append('admin')
psw.append(psw2)
url = "http://127.0.0.1:50000/"
title = "login"
usr_selector = "username"
psw_selector = "password"
submit_selector = "submit"
password_file_path = 'pass.txt'
password_file = open(password_file_path, 'r')

driver = Chrome()
driver.get(url)
assert title in driver.title

for line in password_file:
    elem = driver.find_element_by_name(usr_selector)
    elem.clear()
    elem.send_keys(user[0])
    print('trying with: ', line)
    elem0 = driver.find_element_by_name(psw_selector)
    elem0.clear()
    elem0.send_keys(line)
    driver.find_element_by_name(submit_selector).click()
    assert "No results found." not in driver.page_source
