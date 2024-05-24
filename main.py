import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree Traversal
# Commanly used type of objects:
# 1. Tag                 print(type(title))
# 2. NavigavleString     print(type(title.string))
# 3. BeautifulSoup       print(type(soup))
# 4. Comment             bs4.element.Comment  

# Get the title of the HTML page:
title = soup.title

# Get all the paragraph from the page:
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the page:
anchors = soup.find_all('a')
# print(anchors)
all_links = set()
count = 0
# Get all the links on the page:
for link in anchors:
    if(link != '#'):
        count = count + 1
        linkText = "https://books.toscrape.com/"+link.get('href')
        all_links.add(link)
#         print(linkText)
# print(count)

# Get first element in HTML page:
# print(soup.find('p'))
# print(soup.find('p')['class'])

# Find all the elements with class <class_name> :
# print(soup.find_all("p", class_="star-rating"))

# Get the text from the tags/soup:
# print(soup.find('a').get_text())

# Comment:
markup = "<p><!-- this a comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
print(type(soup2.p.string))