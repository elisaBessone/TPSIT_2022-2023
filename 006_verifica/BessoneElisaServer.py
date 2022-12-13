from socket import socket, AF_INET, SOCK_STREAM
from BessoneElisaFile import File
from BessoneElisaComandi import Comandi
#dimensione del buffer
BUFFER_SIZE = 4096


def run_server(host, port):
    #mi connetto al socket tramite i parametri presi da file
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("server listen...")

        #accetto più connessioni. se viene inviato il messaggio esci il server finsice di funzionare.
        while True:
            client, address = s.accept()
            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode('utf-8')
            print(msg)

            #splitto il messaggio che ricevo in modo tale da avere il comando ricevuto in posizione 0 dal client
            msg_split = msg.split(';')
            comando = msg_split[0]
            print(f"COMANDO RICEVUTO> {comando}.")
            #controllo del comando ricevuto
            #se ricevo SALVA appendo alla lista il nome utente e il messaggio ricevuto
            if comando == Comandi.SALVA:
                nome_utente = msg_split[1]
                message = msg_split[2]
                lista.append((nome_utente, message))
                print(f"Aggiungo alla lista \nLISTA AGGIORNATA>> {lista}.")
            elif comando == Comandi.LEGGI:
                #se la dimensione della lista è 0 invio un messaggio di errore perché il mio 
                if len(lista) == 0:
                    error = "ERRORE. Lista vuota." 
                    client.sendall(error.encode("utf-8"))
                    print(error)
                #altrimento estraggo primo elemento dalla lista e lo invio al client
                else:
                    primo_elemento = str(lista.pop(0))
                    print(f"leggo -->{primo_elemento}, LISTA --> {lista}")
                    elemento = primo_elemento.encode('utf-8')
                    client.sendall(elemento)
                    print(f"PRIMO ELEMENTO> {primo_elemento}. \nLISTA AGGIORNATA>> {lista}.")
            #se invio il comando esci il server smette di accettare connessione. AGGIUNTA
            elif comando == Comandi.ESCI:
                print("Programma terminato.")
                break




if __name__ == "__main__":
    lista = []
    nome_file = "BessoneElisaConfserver.txt"
    host, port = File.leggiFile(nome_file)
    run_server(host, port)