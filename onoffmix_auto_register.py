from selenium import webdriver

email = "testtesttest"
pw = "testtesttest"


browser = webdriver.Firefox()
browser.get("http://www.onoffmix.com/account/login")

emailBox = browser.find_element_by_id("email")
emailBox.send_keys(email)

pwBox = browser.find_element_by_id("pw")
pwBox.send_keys(pw)

loginBtn = browser.find_element_by_class_name("buttonLogin")
loginBtn.click()


