#This program finds all the HTML <p> tags and counts them before printing the sum.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

paragraph = soup('p')
for p in paragraph:
    count = count + 1
    #print(p)

print (count)