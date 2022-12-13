from socket import socket, AF_INET, SOCK_STREAM
import threading
import time



def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    
    client.sendall("4*5".encode("utf-8"))
    #ricevo il messaggio
    risposta = client.recv(4096)
    print(risposta.decode("utf-8"))


if __name__ == "__main__":
    main()