import socket  # for sockets
import sys  # for exit
"""
Extra info:
TCP needs connection because connection means reliable stream.
But rest of them, like UDP , ARP , ICMP dont have a concept of "connection". 
These are connectionless. It means that you can keep sending or receiving packets from 
anybody and everybody as long as you want.
"""

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

host = 'www.wikipedia.com'
port = 80
#try to change port number, if its not open you wouldn't be connect. Logic for port scanner.

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    # could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

# Connect to remote server
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip
