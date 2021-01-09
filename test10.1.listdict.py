
#Program that prints out the mail address with the most emails sent along with the correct amount
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
      line = line.rstrip()  #removes \n from lines
      line = line.split()   #splits line into words
      line = line[1:2]      #puts the second word into line 
      line = (' '.join(line)) #converts list to string
      di[line] = di.get(line,0) + 1   #makes a histogram of line into a dict

#Sort dict by value
lst = list()    #empty list
for key,val in list(di.items()): #for key and value in list - and points to ITEMS in dict
  lst.append((val,key))   #Give key and value the ITEMS and store the two values in ITEMS in KEY and VAL

lst.sort(reverse=True)      #Makes the result descending

for key,val in lst[0:1]:   #for the top key and val.
  print (val,key)         #print the fucker
