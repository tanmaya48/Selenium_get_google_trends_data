from selenium import webdriver 
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import shutil
import sys
import os

opts = Options()

opts.headless=False

fp = webdriver.FirefoxProfile()

fp.set_preference('browser.helperApps.neverAsk.saveToDisk','text/csv,application/pdf')
fp.set_preference('browser.starting.managershowWhenStarting',False)
fp.set_preference('browser.download.dir',os.getcwd())
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

browser = Firefox(options=opts,firefox_profile = fp)


browser.get('https://trends.google.com/trends/?geo=IN')

##search_form = browser.find_element_by_id('search_form_input_homepage')
##search_form.send_keys(name)
##search_form.submit()

browser.implicitly_wait(2)

search = 'cricket'


browser.find_element_by_xpath('//*[@id="input-254"]').send_keys(search)

browser.find_element_by_xpath('//*[@id="input-254"]').send_keys(Keys.ENTER)

browser.implicitly_wait(5)

browser.find_element_by_class_name('widget-actions-item').click()

browser.implicitly_wait(2)

browser.close()	
	

