#Make a program that accepts user inputs and connects to URL and retrieves the information.
import socket

usinp = input ('Enter URL here: ')
usinpspl = usinp.split('/')
usinpspl = usinpspl[2:3]
usinpspl = (str(usinpspl))
usinpspl = usinpspl[2:-2]


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((usinpspl, 80))       #Connects to port 80
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(usinp).encode()
    #Format usinp lets you use curly braces to use variable in string.
    mysock.send (cmd)


    while True:
        data = mysock.recv (512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('Could not open: ',usinp,'please try another URL')

#http://data.pr4e.org/romeo.txt (for validating code)