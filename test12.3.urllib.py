import urllib.request, urllib.parse, urllib.error

user_input = input ('Enter URL code here: ')

fhand = urllib.request.urlopen(user_input)

result = fhand.read()
print (result.decode()[:3000])
print (len(result.decode()))

#asks user for URL and then prints out the 3000 first characters + the total amount of characters as number.