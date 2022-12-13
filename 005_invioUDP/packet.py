class Packet:
    INIZIO = 0
    CONTINUA = 1 
    FINE = 2

    def __init__(self, blocco, stato):
        self.blocco = blocco
        self.stato = stato

    def to_bytes(self):
        print(b"".join([self.stato.to_bytes(1, 'big'),  #1 - 2 --> quanti bytes dedico alla variabile
                len(self.blocco).to_bytes(2, 'big'), self.blocco]))
        return b"".join([self.stato.to_bytes(1, 'big'),  #1 - 2 --> quanti bytes dedico alla variabile
                len(self.blocco).to_bytes(2, 'big'), self.blocco])

    @staticmethod
    def from_bytes(buffer):           #non passo il self perché è un metodo statico
        stato = int.from_bytes(buffer[ : 1], 'big') #metto :1 perché prendo un bytes per via della dimensione che ho definito sopra
        lung = int.from_bytes(buffer[1 : 3], 'big')
        blocco = buffer[3 : 3+lung]    #parto da dove ho finito prima e arrivo fino alla lunghezza più quella posizione
        print(stato, lung, blocco)
        return Packet(blocco, stato)



if __name__ == "__main__":
    pkt = Packet(b'ciao', Packet.INIZIO)
    buffer = pkt.to_bytes()
    pkt2 = pkt.from_bytes(buffer) 
    assert(pkt.stato == pkt2.stato)
    assert(pkt.blocco == pkt2.blocco)
    