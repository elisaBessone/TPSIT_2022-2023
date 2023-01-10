from socket import socket, AF_INET, SOCK_STREAM
import threading
import time



def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))

    while True:
        #chiedo di che numero l'utente vuole fare la tabellina.
        operazione = input("Di quale numero vuoi fare la tabellina? (exit per uscire)>>")
        client.sendall(operazione.encode("utf-8"))

        #se invia il comando exit finisce la connessione con il server
        if operazione.upper() == "EXIT":
            print("Chiusura connessione con il server...")
            client.close()
            break
        #riceve per 11 volte il numero del calcolo della tabellina
        for i in range(0,11):
            #ricevo il messaggio
            risposta = client.recv(4096)
            
            #se mi arriva errore chiudo la connessione con il server
            if risposta.decode("utf-8").upper() == "ERROR":
                print("Error...")
                break 
            else:
                print(risposta.decode("utf-8"))
    

if __name__ == "__main__":
    main()

