from socket import socket, AF_INET, SOCK_STREAM

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024 

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client, clientAddress = s.accept()
    
    msg = client.recv(BUFFER_SIZE).decode('utf8')  #null, bytes 
    print(msg)