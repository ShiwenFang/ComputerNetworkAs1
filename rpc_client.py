import socket
import sys
import random

NUM_TRANSMISSIONS = 10

if len(sys.argv) > 4 or len(sys.argv) < 3:
    print("Usage: python3 " + sys.argv[0] + " server_address server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 4:
    random_seed = int(sys.argv[3])
    random.seed(random_seed)

server_address = sys.argv[1]
server_port = int(sys.argv[2])

# TODO: Create a datagram socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("for loop will start")
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    data = random.randint(0, 100)
    print(f"for loop {i} started")
    # TODO: encode this data somehow (representing the integer as a string is fine)
    rpc_data = f"prime({data})".encode()
    print(f"will send: prime({data})")
    print(f"Will send: prime encode: ({rpc_data})")
    # TODO: Send RPC request (i.e., rpc_data) to the server
    client_socket.sendto(rpc_data, (server_address, server_port))
    print(f"sent: prime({data})")
    print(f"sent to server_address: ({server_address})")
    # TODO: Receive result back from the server into the variable result_data
    result_data, _ = client_socket.recvfrom(1024)

    # TODO: Display it in the format "prime: yes" or "prime: no"
    print(f"sent: prime({data})")
    print(f"prime: {result_data.decode()}")

# TODO: Close any sockets that are open
client_socket.close()
