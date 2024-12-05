###
# Web-Scrapper
# Amanda L.
# Version 1.0
# 

import requests

class main():
  print('Running web-scrapper-orgs')
  # TO DO: Make a request to a website
  site = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
  # print(site)
  print(site.content)

if __name__ == '__main__':
  main()