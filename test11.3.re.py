#Prints out the average of the total numbers found in the document.

import re

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()


lst = list()
for line in fhand:
    line = line.rstrip()
    if re.search('[ ]*', line):
      anum = re.findall('([0-9]+)', line)
      for numb in anum:
        numb = (int(numb))
        lst.append(numb)
         
#totline = len(lst)
tot = sum(lst)
print (tot)


