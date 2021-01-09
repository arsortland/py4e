import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() #opens and reads the URL
fhand = open('cover3.jpg', 'wb') #opens the .jpg. wb is for binary write only
fhand.write(img) #writes the .jpg to disk
fhand.close() #closes the connection

#alternative for bigger files to iterate and not use all main memory:

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()