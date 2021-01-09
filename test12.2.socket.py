#Make a program that counts the full amount of characters but only displays the 3000 first.
import socket

usinp = input ('Enter URL here: ')
usinpspl = usinp.split('/')
usinpspl = usinpspl[2:3]
usinpspl = (str(usinpspl))
usinpspl = usinpspl[2:-2]

count = 0

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((usinpspl, 80))       #Connects to port 80
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(usinp).encode()
    #Format usinp lets you use curly braces to use variable in string.
    mysock.send (cmd)


    while True:
        data = mysock.recv (5120)
        if len(data) < 1:
            break
        count = count + len(data)
        finaldata = data[:3000]
        print (finaldata.decode())

    print (count)
    mysock.close()
except:
    print('Could not open: ',usinp,'please try another URL')

