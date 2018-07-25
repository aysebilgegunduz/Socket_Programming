# Socket client example in python

import socket  # for sockets

# create an AF_INET, STREAM socket (TCP)
#AF_INET : Address Family(IPv4)
#SOCK_STREAM : connection oriented TCP protocol
#SOCK_DGRAM : for UDP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Socket Created'