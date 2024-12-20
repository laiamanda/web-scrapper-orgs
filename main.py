###
# Web-Scrapper
# Amanda L.
# Version 1.0
# 

import requests
from bs4 import BeautifulSoup

class main():
  print('Running web-scrapper-orgs')

  url = 'https://realpython.github.io/fake-jobs/'
  #  url = 'https://en.wikipedia.org/wiki/Category:Non-profit_organizations_based_in_the_United_States'
  headers = {'User-Agent': 'Mozilla/5.0'}

  # Make a request to a website
  site = requests.get(url, headers=headers) 
  
  # If the request failed, then program terminates
  if site.status_code != 200:
    print('[ERROR] Request failed')
    exit(0)

  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(site.content, 'html.parser')

  results = soup.find(id='ResultsContainer') # id mw-pages 
  # print(results.prettify())

  job_cards = results.find_all('div', class_='card-content')

  for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    
    print(title_element)
    print(company_element)
    print(location_element)


if __name__ == '__main__':
  main()