###
# Web-Scrapper
# Amanda L.
# Version 1.0
# 

import requests
from util import fileHandling
from bs4 import BeautifulSoup

class main():
  print('Running web-scrapper-orgs')

  # fileHandling.insertIntoFile("test")

  # url = 'https://realpython.github.io/fake-jobs/'
  # url = 'https://en.wikipedia.org/wiki/Web_scraping'
  url = 'https://en.wikipedia.org/w/index.php?title=Category:Non-profit_organizations_based_in_the_United_States&pagefrom=Watch+Duty#mw-pages'
  # 'https://en.wikipedia.org/wiki/Category:Non-profit_organizations_based_in_the_United_States'
  headers = {'User-Agent': 'Mozilla/5.0'}

  # Make a request to a website
  site = requests.get(url, headers=headers) 
  
  # If the request failed, then program terminates
  if site.status_code != 200:
    print('[ERROR] Request failed')
    exit(0)

  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(site.content, 'html.parser')
  pages = soup.find(id='mw-pages').find_all('li')

  try: 
    for page in pages:
      # Manually insert it into a text file
      fileHandling.insertIntoFile(page.get_text())
  except Exception as error :
    print(error)

if __name__ == '__main__':
  main()