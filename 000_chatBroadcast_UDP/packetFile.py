#Bessone Elisa      classe 5BROB
#creazione di una chat UDP

from dataclasses import dataclass


class Packet:
    NEW_FILE = 0
    GO_ON = 1
    END_FILE = 2

    def __init__(self, status, file):
        #validazione username e messagge
        self.status = status
        self.file = file
    
    def to_bytes(self):
        buffer = b''
        status= self.status.to_bytes(1, 'big')    #?big--> cifra più significativa come prima
        size = len(self.data)
        size = size.to_bytes(1, 'big')
        buffer = status + size + self.data

        return buffer      

    @staticmethod       #non metto il self perché non ho l'istanza dell'oggetto
    def from_bytes(buffer):
        status = int.from_bytes(buffer[:1], 'big')
        size = buffer[1:3].decode('utf-8')
        data = buffer[3:3+size]
        return Packet(status, size)

def run_tests():
    pkt0 = Packet("user", "message")
    pkt1 = pkt0.from_bytes(pkt0.to_bytes())
    assert(pkt0.message == pkt1.message)    #genera errore se nn è True
    assert(pkt0.username == pkt1.username)    #genera errore se nn è True
    #-> TEST UNITARI, test su una singola funzione

if __name__ == "__main__":
    run_tests()