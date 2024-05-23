import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"

#Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Step 3: HTML Tree Traversal
title = soup.title
print(type(title))