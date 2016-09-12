import time
import datetime
from selenium import webdriver

email = ""
pw = ""

# onoffmix, facebook
login_type = "onoffmix"
meetup_url = "http://onoffmix.com/event/76453"


# 2016년 9월 28일 15시 30분 
reserve_date = datetime.datetime(2016, 9, 28, 15, 30)


browser = webdriver.Firefox()
browser.get("http://www.onoffmix.com/account/login")

if login_type == "onoffmix":
    email_box = browser.find_element_by_id("email")
    email_box.send_keys(email)

    pw_box = browser.find_element_by_id("pw")
    pw_box.send_keys(pw)

    login_btn = browser.find_element_by_class_name("buttonLogin")
    login_btn.click()
elif login_type == "facebook":
    time.sleep(1)
    facebookBtn = browser.find_element_by_css_selector("li.facebook > a")
    facebookBtn.click()

    email_box = browser.find_element_by_name("email")
    email_box.send_keys(email)

    pw_box = browser.find_element_by_name("pass")
    pw_box.send_keys(pw)

    login_btn = browser.find_element_by_id("loginbutton")
    login_btn.click()

time.sleep(0.3)
print(reserve_date)
while True:
    if datetime.datetime.now() < reserve_date:
        time.sleep(1)
    else:
        browser.get(meetup_url)
        break
    
register_btn = browser.find_element_by_class_name("ofmBtn")
register_btn.click()

final_register_btn = browser.find_element_by_class_name("ofmBtn")
final_register_btn.click()

