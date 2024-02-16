import sys
import signal
import sys
import select
from socket import *
import builtins

if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[0] + "server_address server_port")
    sys.exit(1)

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

server_address = sys.argv[1]
relay_port = int(sys.argv[2])

# Create a socket for the sender
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect sender to the server at the server_port
client_socket.connect((server_address, relay_port))

# Set up a list of file descriptors to read from
stdin = sys.stdin.fileno()
all_fds = [stdin] # Add your sockets fileno() here
all_fds.append(client_socket.fileno())

# Repeat until server goes down or user stops entering in data
while True:
    ready_fds, _, _ = select.select(all_fds, [], [], 5)

    for fd in ready_fds:
        if fd == stdin:
            # Send data if you stdin is in ready_fds (i.e. if user pressed enter)
            user_input = sys.stdin.readline()
            client_socket.sendall(user_input.encode())
        elif fd == client_socket.fileno():
            # Receive data if socket fileno is in ready_fds
            message = client_socket.recv(1024)
            if not message:
                print("Server closed the connection.")
                break
            print(f"Received: {message.decode()}")

# Close the socket
client_socket.close()
