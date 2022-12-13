import sys
from socket import socket, AF_INET, SOCK_STREAM
BUFFER_SIZE = 4096

class Opzioni():
    def __init__(self, portaServer, host, porta):
        self.portaServer = int(portaServer)
        self.host = host
        self.porta = int(porta)
    
    def get_socket(self):
        return self.host, self.porta

def richiedi_dati(sock, percorso):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((sock))
        s.sendall(f"GET {percorso}.json HTTP/1.0\n\n".encode("utf-8"))      #"".format()
        #quesro while true accetta più dati in modo tale che se ci sono più dati 
        #li prendo tutti
        
        data = s.recv(BUFFER_SIZE)
        data = data + s.recv(BUFFER_SIZE)

        """dati = []
        data = True
        while data:
            data = s.recv(BUFFER_SIZE)
            if data:
                dati.append(data)
        dati = b''.join(dati)"""
    
    return data


def main(args):
    #punto 1: prendo parametri da riga di comando.
    opt = Opzioni(args[1], args[2], args[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        #punto 2: 
        s.bind(("0.0.0.0", opt.portaServer))
        s.listen()
        while True:
            client, client_addr = s.accept()
            data = client.recv(BUFFER_SIZE)
            data = data.decode("utf-8")
            campi = data.split(" ")
            #richiesta_http = campi[1] + ".json"
            dati = richiedi_dati(opt.get_socket(), campi[1])
            print(dati.decode("utf-8"))

            client.sendall(dati)

if __name__ == "__main__":
    main(sys.argv)