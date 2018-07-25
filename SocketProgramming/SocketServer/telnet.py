"""
1. Listen for incoming messages from the server.
2. Check user input. If the user types in a message then send it to the server.
Now here is something tricky. The client has to actually listen for server message and user input at the same time. 
To do this, we use the select function.
When a message comes from the server on the connected socket, 
it is readable and when the user types a message and hits enter, the stdin stream is readable.

select function has to monitor 2 streams. First is the socket that is connected to the remote webserver, 
and second is stdin or terminal input stream. The select function blocks till something happens. 
So after calling select, it will return only when either the server socket receives a message or the user enters a 
message. If nothing happens it keeps on waiting.
"""

# telnet program example
import socket, select, string, sys


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


# main function
if __name__ == "__main__":

    if (len(sys.argv) < 3):
        print 'Usage : python telnet.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()

    print 'Connected to remote host. Start sending messages'
    prompt()

    while 1:
        #in this case, the read_sockets array will contain either the server socket, or stdin or both
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt()

            # user entered a message
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()