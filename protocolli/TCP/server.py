from Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 7000


def run_server():

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))

        s.listen()
  
        client, clientAddress = s.accept()
        running = True
        while running:
            msg = client.recv(MAX_SIZE)
            

if __name__ == "__main__":
    run_server()