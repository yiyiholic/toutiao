chromdriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"

from selenium import webdriver
import time
import re
from urllib.parse import urlencode

def get_signature(offset):
	
	option = webdriver.ChromeOptions()
	option.add_experimental_option("excludeSwitches",["enable-automation"])
	driver =webdriver.Chrome(options=option)
	driver.get(url= "http://localhost/?offset="+str(offset))
	time.sleep(0.5)
	driver.refresh()
	page=driver.page_source
	res=re.search(r'<script src="jrtt.js"></script>(.*?)<script>',page,re.S)
	res=res.group(1).strip().split('<br>')
	driver.delete_all_cookies()
	driver.quit()
	
	return res
