###
# Web-Scrapper
# Amanda L.
# Version 1.0
# 

import requests
from util import fileHandling
from bs4 import BeautifulSoup

# import util.fileHandling

class main():
  print('Running web-scrapper-orgs')

  fileHandling.findOrgsFile()

  # fileHandling.insertIntoFile()

  # # url = 'https://realpython.github.io/fake-jobs/'
  # # url = 'https://en.wikipedia.org/wiki/Web_scraping'
  # url = 'https://en.wikipedia.org/wiki/Category:Non-profit_organizations_based_in_the_United_States'
  # headers = {'User-Agent': 'Mozilla/5.0'}

  # # Make a request to a website
  # site = requests.get(url, headers=headers) 
  
  # # If the request failed, then program terminates
  # if site.status_code != 200:
  #   print('[ERROR] Request failed')
  #   exit(0)

  # # Use BeautifulSoup to parse the HTML
  # soup = BeautifulSoup(site.content, 'html.parser')
  # pages = soup.find(id='mw-pages').find_all('li')

  # try: 
  #   for page in pages:
  #     text = page.get_text().encode('utf-8')
  #     # TO DO: Find a way to decode it but allowing all character to pass thur from multiple different languages
  #     # that's not supported by
  #     # Manually insert it into a text file and configure the names from there, because unable to decode it
  #     print(text)
  # except Exception as error :
  #   print(error)
    
  ### DEVELOPMENT ###
  # Use BeautifulSoup to parse the HTML
  # soup = BeautifulSoup(site.content, 'html.parser')

  # results = soup.find(id='ResultsContainer') # id mw-pages 
  # # print(results.prettify())

  # job_cards = results.find_all('div', class_='card-content')

  # for job_card in job_cards:
  #   title_element = job_card.find("h2", class_="title")
  #   company_element = job_card.find("h3", class_="company")
  #   location_element = job_card.find("p", class_="location")
    
  #   print(title_element)
  #   print(company_element)
  #   print(location_element)


if __name__ == '__main__':
  main()