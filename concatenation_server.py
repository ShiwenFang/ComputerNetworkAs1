# TODO: import socket library
import socket

import sys
import random
import string

# Random alphanumeric string. Do not change
def rand_str(l):
    ret = ""
    for i in range(l):
        ret += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    return ret

if (len(sys.argv) > 3) or len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 3:
    random_seed = int(sys.argv[2])
    random.seed(random_seed)

server_port = int(sys.argv[1])

# TODO: Create a socket for the server on localhost
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: Bind it to a specific server port supplied on the command line
server_socket.bind(('', server_port))

# TODO: Put server's socket in LISTEN mode
server_socket.listen(1)

# TODO: Call accept to wait for a connection
connection_socket, addr = server_socket.accept()

# TODO: receive data over the socket returned by the accept() method

# TODO: print out the received data for debugging

# TODO: Generate a new string of length 10 using rand_str

# TODO: Append the string to the buffer received

# TODO: Send the new string back to the client

# TODO: Exit when client client closes connection

# TODO: Close all sockets that were created
while True:
    received_data = connection_socket.recv(1024)
    if not received_data:
        break

    print(f"Received: {received_data.decode()}")

    random_string = rand_str(10)
    concatenated_data = received_data.decode() + random_string

    connection_socket.send(concatenated_data.encode())

connection_socket.close()
server_socket.close()
