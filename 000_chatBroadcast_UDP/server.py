#Bessone Elisa      classe 5BROB
#creazione di una chat UDP

from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet
BUFFER_SIZE = 1024
HOST = '0.0.0.0'  #!localhost 127.0.0.1, interfaccia particolare (più schede di rete) 0.0.0.0
PORT = 5000

#trasferisco un array di byte --> bytes. 
#da sringa a bytes uso la codifica UTF-8. UNICODE: più grande
#bytes stampa b'ciao', str stampa 'ciao'
#per vedere il tipo type('nomeVariabile')


def chatServer():
    ##* with socket(AF_INET, SOCK_DGRAM) as s:   #per non scrivere s.close() 
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            pkt = Packet.from_bytes(msg[0])
            print(f"L'utente {pkt.username} ha inviato il messaggio {pkt.message}.")


if __name__ == "__main__":
    chatServer()
