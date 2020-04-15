
import urllib.request, urllib.parse, urllib.error

# Import Beautiful Soup
# Beautiful soup is a html parser library used to parse all the HTML even the one having syntax errors
from bs4 import BeautifulSoup

# Not a related topic
# Just in case of certificate errors
import ssl

# Ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Entering the URL
url = input('Enter the URL: ')

# Return the document of the webpage in a single string 
html = urllib.request.urlopen(url, context=ctx).read()

# Parsing the html content 
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

# Here we are getting all the anchor tags
tags = soup('a')
print(type(tags))

for tag in tags:
    # Getting all the links
    print(tag.get('href',None))
