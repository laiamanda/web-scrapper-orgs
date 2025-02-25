"""
  Web Scrapper
  Amanda L.
  Version 1.0

  This program is designed to read a wiki page and
  scrape for non-profit organizations and insert it into a database. 
  It is used for the volunteer dashboard web application
"""

# Import packages
import requests
from util import fileHandling
from bs4 import BeautifulSoup

class main():
  print('Running web-scrapper-orgs')

  url = 'https://en.wikipedia.org/wiki/Category:Non-profit_organizations_based_in_the_United_States'
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
    # Loop through all the pages
    for page in pages:
      # Manually insert the companyName into a text file
      fileHandling.insertIntoFile(page.get_text())
  except Exception as error :
    print("[ERROR]: " + error)

  # Read into the file and insert the text into database
  fileHandling.readFile()

if __name__ == '__main__':
  main()