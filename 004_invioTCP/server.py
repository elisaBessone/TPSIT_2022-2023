from packet import Packet
from socket import socket, AF_INET, SOCK_STREAM
import os

BUFFER_SIZE = 7000

def write_file(buffer):
    with open("risultato.pdf", "wb") as f:
        f.write(buffer)

def run_server():
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))

        s.listen()
        print("Server in ascolto...")

        client, address = s.accept()

        running = True
        while running:
            msg = client.recv(BUFFER_SIZE)
            packet = Packet.from_bytes(msg)
            if packet.status == Packet.NEW_FILE:
                file = []
                print('file creato')

            if packet.data and len(packet.data) > 0:
                file.append(packet.data)
                print("Pacchetto ricevuto")

            if packet.status == Packet.END_FILE:
                print("Ricezione pacchetti eseguita")
                write_file(b''.join(file))
                print("Scrittura su file")
                running = False

if __name__ == "__main__":
    run_server()