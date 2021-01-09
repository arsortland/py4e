import re

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()

numline = 0

for line in fhand:
    line = line.rstrip()
    if re.search('[ ]*', line):
        numline = numline + 1
print ('Number of lines in document: ', numline)

