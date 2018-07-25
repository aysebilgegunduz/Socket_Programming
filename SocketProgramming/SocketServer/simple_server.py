'''
    Simple socket server using threads
'''

import socket
import sys

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
# if 10 connections are already waiting to be processed, then the 11th connection request shall be rejected.
s.listen(10)
print 'Socket now listening'

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

s.close()

#so now this program is waiting for incoming connections on port 8888,don't close keep it RUN!!! :)