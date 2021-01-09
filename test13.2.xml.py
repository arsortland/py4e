import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#line 12 to 14 is the easiest way to open xml in Python afaik.
url = input ('Enter URL - ')
html = urllib.request.urlopen(url,context=ctx).read()
tree = ET.fromstring(html)

lst = tree.findall('comments/comment')
print ('Count',len(lst))

totsum = 0

for item in lst:
    num = int(item.find('count').text)
    totsum = totsum + num
print ('Sum:',totsum)