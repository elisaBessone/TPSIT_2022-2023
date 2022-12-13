#INVIO FILE - PROTOCOLLO UDP 

from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet

BUF_SIZE = 10
def invia_file(sock, dest):
    with open("miofile.txt", 'rb') as f:
        finito = False
        #invio un blocco vuoto perché non ho nessun dato da inviare, devo solo inviare lo stato
        sock.sendto(Packet(b'', Packet.INIZIO).to_bytes(), dest)
        while not finito:
            dati = f.read(BUF_SIZE)
            if dati:
                print(f"DATI:{dati}")
                sock.sendto(Packet(dati, Packet.CONTINUA).to_bytes(), dest)
            else:
                sock.sendto(Packet(b'', Packet.FINE).to_bytes(), dest)
                finito = True

def main():
    destinatario = ('127.0.0.1', 5000)
    with socket(AF_INET, SOCK_DGRAM) as s:
        invia_file(s, destinatario)



if __name__ == "__main__":
    main()
