#Bessone Elisa      classe 5BROB
#creazione di una chat UDP

# |  1 byte (#username)  |  username  |  2 byte (#message)  |  message 

import re


class Packet:
    def __init__(self, username, message):
        #validazione username e messagge
        self.username = username
        self.message = message
    
    def to_bytes(self):
        buffer = b''

        username_bytes = self.username.encode('utf-8')
        username_buffer= len(username_bytes).to_bytes(1, 'big')    #?big--> cifra più significativa come prima
        buffer = buffer + username_buffer + username_bytes

        message_bytes = self.message.encode('utf-8')
        message_buffer= len(message_bytes).to_bytes(2, 'big')
        buffer = buffer + message_buffer + message_bytes

        return buffer      

    @staticmethod       #non metto il self perché non ho l'istanza dell'oggetto
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1:username_size+1].decode('utf-8')

        message_size = int.from_bytes(buffer[username_size+1:username_size+3], 'big')
        message = buffer[username_size+3:username_size+3+message_size+1].decode('utf-8')
        
        return Packet(username, message)

def run_tests():
    pkt0 = Packet("user", "message")
    pkt1 = pkt0.from_bytes(pkt0.to_bytes())
    assert(pkt0.message == pkt1.message)    #genera errore se nn è True
    assert(pkt0.username == pkt1.username)    #genera errore se nn è True
    #-> TEST UNITARI, test su una singola funzione

if __name__ == "__main__":
    run_tests()