#Bessone Elisa      classe 5BROB
#creazione di una chat UDP

from socket import AF_INET, SOCK_DGRAM, socket, SOL_SOCKET, SO_REUSEADDR
from packetFile import Packet
BUFFER_SIZE = 7000
HOST = '0.0.0.0'  #!localhost 127.0.0.1, interfaccia particolare (più schede di rete) 0.0.0.0
PORT = 5000

#trasferisco un array di byte --> bytes. 
#da sringa a bytes uso la codifica UTF-8. UNICODE: più grande
#bytes stampa b'ciao', str stampa 'ciao'
#per vedere il tipo type('nomeVariabile')
def write_file(buffer):
    with open('risultato.pdf', 'wb') as file:
        file.write(buffer)

def chatServer():
    ##* with socket(AF_INET, SOCK_DGRAM) as s:   #per non scrivere s.close() 
    with socket(AF_INET, SOCK_DGRAM) as s:
        #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        file = []
        print('inizio')
        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            #print(msg[0])
            pkt = Packet.from_bytes(msg[0])
            #print(pkt.data)
            if pkt.status == Packet.NEW_FILE:
                file = []
                print('new file')
                #print(file)

            if pkt.data and len(pkt.data) > 0:
                file.append(pkt.data)
                print('pacchetto aggiunto')

            print(f"stato: {pkt.status}, {Packet.END_FILE}")

            if pkt.status == Packet.END_FILE:
                file_completo = b''.join(file)
                write_file(file_completo)   
                print(f"fine file {file_completo}")             
                break


if __name__ == "__main__":
    chatServer()
