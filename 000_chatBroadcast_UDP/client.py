#Bessone Elisa      classe 5BROB
#creazione di una chat UDP
from socket import SOCK_DGRAM, socket, AF_INET, SOCK_STREAM
import sys
"""HOST = "192.168.95.255"  #INDIRIZZO DI BROADCAST PER INVIARE A TUTTA LA RETE
PORT = 5000"""

def chatClient():
    #richiedo indirizzo ip, porta e nome utente
    #print("Client in esecuzione: inserire INDIRIZZO IP, il numero della PORTA e il NOME UTENTE")
    _, host, port, nome = sys.argv
    print(host, port, nome)
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            utente = "L'utente: " + nome + ' ha inviato il messagio: '
            msg = input("Inserire il messaggio da inviare: (se vuoi chiudere la connessione clicca )")   
            #msg = "hello world"

            if (msg.upper() == "EXIT"):     #! se voglio disconnettermi scrivo exit
                break
            
            msg = utente + msg
            msg = msg.encode('utf8') 
            
            s.sendto(msg, (host, int(port)))

        print("Connessione chiusa")

if __name__ == '__main__':
    chatClient()