# Imports

from selenium import webdriver
import time
import re

#Web scrapering

l=list()
o={}

target_url = "https://www.randomlists.com/email-addresses"

driver=webdriver.Chrome()
driver.get(target_url)

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
html = driver.page_source
emails = re.findall(email_pattern, html)

time.sleep(10)
print(emails)
driver.close()