import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Easiest way to open json afaik. .loads converts json to python.
data = input ('Enter URL: ')
html = urllib.request.urlopen(data,context=ctx).read()

info = json.loads(html)

tot = 0
y = 0
#two lines under is how to iterate a list inside a dict.
for k in info:
    for x in info[k]:
        try:
            num = int(info['comments'][y]['count'])
            y +=1
        except:
            continue
        tot = tot + num
print (tot)