# Print out only the domain name of emails used in mbox document.
fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')
    exit()

di = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
      line = line.split()
      line = line[1:2]
      line = " ".join(line)
      domain = line.split('@')[1] 
      di[domain] = di.get(domain,0) + 1 #See 9.3 for explanation

print (di)