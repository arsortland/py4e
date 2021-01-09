fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
  fhand =  open(fname)
except:
    print ('File', fname, 'not found')

di = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        line = line[1:2]
        line = "".join(line)
        di[line] = di.get(line,0) + 1 #takes the value to 0 the first time and adds 1 to it the next time(s).

#print (di)

largest = -1
theword = None
for k,v in di.items() :

    if v > largest :
        largest = v
        theword = k
        
print (theword, largest)


