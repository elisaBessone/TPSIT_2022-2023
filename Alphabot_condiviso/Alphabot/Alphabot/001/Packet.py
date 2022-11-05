#Bessone Elisa      classe 5BROB
#creazione di una chat UDP

# |  1 byte (#movimento)  |  movimento  |  2 byte (#durata)  |  durata 

import re


class Packet:
    def __init__(self, movimento, durata):
        #validazione movimento e messagge
        self.movimento = movimento
        self.durata = durata
    
    def to_bytes(self):
        buffer = b''

        movimento_bytes = self.movimento.encode('utf-8')
        movimento_buffer= len(movimento_bytes).to_bytes(1, 'big')    #?big--> cifra più significativa come prima
        buffer = buffer + movimento_buffer + movimento_bytes

        durata_bytes = self.durata.encode('utf-8')
        durata_buffer= len(durata_bytes).to_bytes(2, 'big')
        buffer = buffer + durata_buffer + durata_bytes

        return buffer      

    @staticmethod       #non metto il self perché non ho l'istanza dell'oggetto
    def from_bytes(buffer):
        movimento_size = int.from_bytes(buffer[0:1], 'big')
        movimento = buffer[1:movimento_size+1].decode('utf-8')

        durata_size = int.from_bytes(buffer[movimento_size+1:movimento_size+3], 'big')
        durata = buffer[movimento_size+3:movimento_size+3+durata_size+1].decode('utf-8')
        
        return Packet(movimento, durata)

def run_tests():
    pkt0 = Packet("user", "durata")
    pkt1 = pkt0.from_bytes(pkt0.to_bytes())
    assert(pkt0.durata == pkt1.durata)    #genera errore se nn è True
    assert(pkt0.movimento == pkt1.movimento)    #genera errore se nn è True
    #-> TEST UNITARI, test su una singola funzione

if __name__ == "__main__":
    run_tests()