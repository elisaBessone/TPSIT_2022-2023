from socket import socket, AF_INET, SOCK_STREAM
import threading
import time



def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    
    while True:
        operazione = input("Inserisci l'operazione (EXIT per finire il programma)>>")
        client.sendall(operazione.encode("utf-8"))

         #ricevo il messaggio
        risposta = client.recv(4096)
        #print(risposta.decode("utf-8"))

        if risposta.decode("utf-8").upper() == "EXIT":
            print("CHiusura connessione con il server...")
            client.close()
            break
        else:
            print(risposta.decode("utf-8"))
   


if __name__ == "__main__":
    main()