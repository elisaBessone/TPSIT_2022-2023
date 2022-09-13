#Bessone Elisa      classe 5BROB
#creazione di una chat UDP
from socket import SOCK_DGRAM, socket, AF_INET, SOCK_STREAM

HOST = "192.168.95.255"  #INDIRIZZO DI BROADCAST PER INVIARE A TUTTA LA RETE
PORT = 5000

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
    
        msg = "hello world"
        
        msg = msg.encode('utf8')

        s.sendto(msg, (HOST, PORT))


if __name__ == '__main__':
    chatClient()