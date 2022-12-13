from Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM


def run_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        
        s.send()
        

if __name__ == "__main__":
    run_client()