import sys
import select
from socket import *

import builtins

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

bad_words = ["virus", "worm", "malware"]
good_words = ["groot", "hulk", "ironman"]

def replace_bad_words(s):
    for j in range(3):
        s = s.replace(bad_words[j], good_words[j])
    return s

if len(sys.argv) != 2:
    print("Usage: python3 " + sys.argv[0] + " port")
    sys.exit(1)
port = int(sys.argv[1])

# Create a TCP socket to listen on port for new connections
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(5)

# Bind the server's socket to port
input_sockets = [server_socket]
client_addresses = {}

# Put listener_socket in LISTEN mode

# Accept a connection first from two clients
# OR 
# implement accepting connections from multiple clients
# by including listener_socket in event handling 


active = True

while active:
    pass
    # Use select to see which socket is available to read from

    # recv on socket that is ready to read

    # Check to see if connection is closed

    # Filter and replace bad words

    # Forward to other sockets
    readable_sockets, _, _ = select.select(input_sockets, [], [], 1)

    for sock in readable_sockets:
        if sock is server_socket:
            # Handle new connections
            client_socket, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            input_sockets.append(client_socket)
            client_addresses[client_socket] = addr
        else:
            # Receive and process messages from clients
            message = sock.recv(1024)
            if not message:
                print(f"Closing connection with {client_addresses[sock]}")
                sock.close()
                input_sockets.remove(sock)
                del client_addresses[sock]
            else:
                # Filter and replace bad words
                modified_message = replace_bad_words(message.decode())

                # Forward to other sockets
                for client in input_sockets:
                    if client not in [server_socket, sock]:
                        client.send(modified_message.encode())

# Close sockets
for sock in input_sockets:
    sock.close()
