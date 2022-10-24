from socket import socket, AF_INET, SOCK_STREAM

HOST = "localhost"
PORT = 5000

with socket(AF_INET, SOCK_STREAM) as s:
    server = s.connect((HOST, PORT))
    server.send("dati".encode('utf8'))
    

