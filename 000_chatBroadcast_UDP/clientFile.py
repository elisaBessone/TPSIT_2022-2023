#Bessone Elisa      classe 5BROB
#creazione di una chat UDP
"""Realizzare un applicazione python che invii un file (binario) attraverso UDP. 
Il file va suddiviso in pacchetti di dimensione fissa e inviare un pacchetto alla volta 
(per esempio inviare 4KB alla volta).
Ogni pacchetto dovrà includere la sua lunghezza (saranno tutti di 4KB, ma l'ultimo potrebbe essere più piccolo) 
ed è necessario stabilire quando tutti i pacchetti sono stati inviati."""

from socket import SOCK_DGRAM, socket, AF_INET
from struct import pack
from packet import Packet
"""HOST = "192.168.95.255"  #INDIRIZZO DI BROADCAST PER INVIARE A TUTTA LA RETE
PORT = 5000"""

def input_value():
    host = input("Inserisci l'indirizzo ip: ")
    port = int(input("Inserisci la porta: "))
    name = input("Inserisci il nome utente: ")

    print(host, port, name)
    return host, port, name

def chatClient(host, port, name):
    #richiedo indirizzo ip, porta e nome utente
    #print("Client in esecuzione: inserire INDIRIZZO IP, il numero della PORTA e il NOME UTENTE")
    receiver = (host, port)
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("input.pdf", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b'').to_bytes(), receiver)

            while True:
                data = True
                while data:
                    data = f.read(4096)                    
                    if data:
                        s.sendto(Packet(Packet.GO_ON,b'').to_bytes(), receiver)
                s.sendto(Packet(Packet.END_FILE, b'').to_bytes(), receiver)

if __name__ == '__main__':
    host, port, name = input_value()

    chatClient(host, port, name)