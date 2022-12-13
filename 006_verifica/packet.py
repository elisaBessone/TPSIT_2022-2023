
class Packet:
    def __init__(self, comando, utente, messaggio):
        self.comando = comando
        self.utente = utente
        self.messaggio = messaggio

    def encode(self):
        ris = f"{self.comando}; {self.utente}; {self.messaggio}"
        return ris.encode()

    @staticmethod
    def decode(buffer):
        str_packet = buffer.decode()
        campi = str_packet.split(";")
        comando, utente, messaggio = campi[0], campi[1], campi[2]
        return Packet(comando, utente, messaggio)