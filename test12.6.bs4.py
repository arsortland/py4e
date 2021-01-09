import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input ('Enter count: '))
pos = int(input ('Enter position: '))
pos = pos - 1
#lst = []
tags = soup('a')

for i in range (count):       #Determines how many times we repeat the loop
    link = tags[pos].get('href', None)  #We index which link we want with [] and gets the href from it.
    print ('Retrieving: ', link)    #Prints that pos link
    #lst.append(tags[pos].contents[0]) #the [0] makes it int and not list?]
                                #While also appending the name(content in the link to the list)
    html = urllib.request.urlopen(link, context=ctx).read() #Saves the link found in count to html for the next iteration
    soup = BeautifulSoup(html, 'html.parser') 
    tags = soup ('a')

#print (lst[-1])