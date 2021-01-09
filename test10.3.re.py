import re

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()

di = dict()
for line in fhand:
    line = line.lower()
    res1= ''.join(re.split("[^a-zA-Z]*" ,line))
    for word in res1:
        di[word] = di.get(word,0) + 1

lst = list()

for k,v in list (di.items()):
    lst.append((v, k))

lst.sort()

for k, v in lst:
    print (k,v)
