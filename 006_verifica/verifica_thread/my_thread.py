import threading
import socket
import time
from comandi import Comandi

class ThreadComandi(threading.Thread):
        #conn: per rispondere ho bisogno del riferimento all'oggetto, la connessione
    def __init__(self, conn, lista):
        threading.Thread.__init__(self, name="Thread comando.")
        self.conn = conn
        self.lista = lista

    #ereditarietà multipla. posso ereditare più classi
    def run(self):
        msg = self.conn.recv(4096).decode('utf-8')
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
            self.lista.append((nome_utente, message))
            print(f"Aggiungo alla lista \nLISTA AGGIORNATA>> {self.lista}.")
        elif comando == Comandi.LEGGI:
            #se la dimensione della lista è 0 invio un messaggio di errore perché il mio 
            if len(self.lista) == 0:
                error = "ERRORE. Lista vuota." 
                self.conn.sendall(error.encode("utf-8"))
                print(error)
            #altrimento estraggo primo elemento dalla lista e lo invio al client
            else:
                primo_elemento = str(self.lista.pop(0))
                print(f"leggo -->{primo_elemento}, LISTA --> {self.lista}")
                elemento = primo_elemento.encode('utf-8')
                self.conn.sendall(elemento)
                print(f"PRIMO ELEMENTO> {primo_elemento}. \nLISTA AGGIORNATA>> {self.lista}.")


