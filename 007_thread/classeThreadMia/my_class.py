import threading
import socket
import time

class MyClassThread(threading.Thread):
        #conn: per rispondere ho bisogno del riferimento all'oggetto, la connessione
    def __init__(self, conn):
        threading.Thread.__init__(self, name="Thread operazione")
        self.conn = conn

    #ereditarietà multipla. posso ereditare più classi
    def run(self):
        while True:
            msg = self.conn.recv(4096). decode('utf-8')
            print(f"{msg} da {threading.current_thread().name}.")

            if msg.upper() == "EXIT":
                print(f"Chiusura connessione con {threading.current_thread().name}")
                self.conn.send(msg.encode('utf-8'))
                self.conn.close()
                break
            else:
                try:
                    result = eval(msg)   #esegue una stringa ricevuta se ci sono dei comandi funzionanti
                    print(f"Risultato {msg}: {result}")
                    self.conn.sendall(str(result).encode("utf-8"))
                except:
                    print("Error")
                    self.conn.send("Error".encode("utf-8"))

