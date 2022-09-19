#Bessone Elisa      classe 5BROB
#creazione di una chat UDP
from socket import SOCK_DGRAM, socket, AF_INET
"""HOST = "192.168.95.255"  #INDIRIZZO DI BROADCAST PER INVIARE A TUTTA LA RETE
PORT = 5000"""

def input_value():
    host = input("Inserisci l'indirizzo ip: ")
    port = int(input("Inserisci la porta: "))
    name = input("Inserisci il nome utente: ")

    print(host, port, name)
    return host, port, name

def chatClient(host, port, name):
    #richiedo indirizzo ip, porta e nome utente
    #print("Client in esecuzione: inserire INDIRIZZO IP, il numero della PORTA e il NOME UTENTE")
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            utente = "L'utente: " + name + ' ha inviato il messagio: '
            msg = input("Inserire il messaggio da inviare: (se vuoi chiudere la connessione scrivi exit )")   
            #msg = "hello world"

            if (msg.upper() == "EXIT"):     #! se voglio disconnettermi scrivo exit
                break
            
            msg = utente + msg
            msg = msg.encode('utf8') 
            
            s.sendto(msg, (host, int(port)))

        print("Connessione chiusa")

if __name__ == '__main__':
    host, port, name = input_value()

    chatClient(host, port , name)