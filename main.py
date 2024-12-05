###
# Web-Scrapper
# Amanda L.
# Version 1.0
# 

import requests
from bs4 import BeautifulSoup

class main():
  print('Running web-scrapper-orgs')

  url = 'https://www.geeksforgeeks.org/python-programming-language/'

  # Make a request to a website
  site = requests.get(url)
  
  # If the request failed, then program terminates
  if site.status_code != 200:
    print('[ERROR] Request failed')
    exit(0)

  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(site.content, 'html.parser')
  # print(soup.prettify(formatter="html").encode('utf-8'))
  s = soup.find('div', class_='entry-content')
  content = soup.find_all('p')

  print(content)

if __name__ == '__main__':
  main()