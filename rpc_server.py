import sys
import signal
import socket

NUM_TRANSMISSIONS = 10
if len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port")
    sys.exit(1)
assert len(sys.argv) == 2
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Setup signal handler to exit gracefully
def cleanup(sig, frame):
    # TODO Close server's socket
    sys.exit(0)

# SIGINT is sent when you press ctrl + C, SIGTERM if you use 'kill' or leave the shell
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)


# TODO: Bind it to server_port
server_socket.bind(('', server_port))

def is_prime(n):
    """Function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    
    # TODO: Receive RPC request from client
    rpc_data, client_address = server_socket.recvfrom(1024)

    # TODO: Turn byte array that you received from client into a string variable called rpc_data
    rpc_data = rpc_data.decode()

    # TODO: Parse rpc_data to get the argument to the RPC.
    # Remember that the RPC request string is of the form prime(NUMBER)
    num = int(rpc_data.split('(')[1].split(')')[0])

    # TODO: Print out the argument for debugging
    print(f"Received number: {num}")

    # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
    response = 'yes' if is_prime(num) else 'no'

    # TODO: Send the result of primality check back to the client who sent the RPC request
    server_socket.sendto(response.encode(), client_address)

# TODO: Close server's socket
# it closes it selve with the cleanup function