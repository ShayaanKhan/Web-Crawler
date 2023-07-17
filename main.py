# Imports

from bs4 import BeautifulSoup
import requests
import lxml

#Web scrapering
# url = 'https://www.fandom.com/?s=games'
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')
# article =   soup.find('div' , class_="grid-content details")
# title =     article.find('h3' , class_="entry-title").text
# author =    article.find('span', class_="author-name").text
# # print(title)
# print(author)

#Web crawlering

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
# html = driver.page_source
# emails = re.findall(email_pattern, html)
# time.sleep(30)
# print(emails)
# driver.close()