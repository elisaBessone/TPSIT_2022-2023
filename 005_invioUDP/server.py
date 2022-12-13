from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet

def scrivi_file(pezzi):
    print(pezzi)

def main():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        finito = False
        while not finito:
            dati, da = s.recvfrom(8096)
            pkt = Packet.from_bytes(dati)
            if pkt.stato == Packet.INIZIO:
                pezzi = []
                print("INIZIO")
            elif pkt.stato == Packet.CONTINUA:
                pezzi.append(pkt.blocco)
                print("CONTINUA")
            else:
                scrivi_file(b''.join(pezzi))
                print("FINE")

if __name__ == '__main__':
    main()