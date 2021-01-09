#Make a program that prints out a ascending list of hours a day emails in the mbox document is sent.
fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()

di = dict()
for line in fhand:
    if line.startswith('From '):
      line = line.rstrip()
      line = line.split()
      line = line[5:6]
      line = ' '.join(line)
      line = line[:2]
      di[line]= di.get(line,0) + 1

lst = list()
for k, v in list(di.items()):
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print(k,v)
