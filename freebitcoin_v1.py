#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, sys
import time


username = ""
password = ""

driver = webdriver.Firefox()
driver.get("https://freebitco.in/")


link = driver.find_element_by_link_text('LOGIN')
link.click()

elem = driver.find_element_by_name("btc_address")
elem.clear()
elem.send_keys(username)
elem.send_keys(Keys.TAB)

time.sleep( 5 )

driver.find_element_by_id("login_form_password").send_keys(password)
driver.find_element_by_id("login_button").click()

time.sleep( 10 )

# get the image source
img = driver.find_element_by_xpath('//*[@id="captchasnet_free_play_captcha"]/div[1]/img')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")


os.system("convert captcha.png -gaussian-blur 0 -threshold 25% -paint 1 captcha_convert.png")
captcha_result = os.popen('tesseract captcha_convert.png -').read()

driver.find_element_by_class_name('captchasnet_captcha_input_box').send_keys(captcha_result)
time.sleep(3)
driver.find_element_by_id("free_play_form_button").click()
driver.close()
