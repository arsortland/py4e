import re

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()

numline = 0
grep= input('Enter a regular expression: ')
for line in fhand:
    line = line.rstrip()
    if re.search(grep, line):
        numline = numline + 1
print ('This file had', numline,'lines that matched', grep)
