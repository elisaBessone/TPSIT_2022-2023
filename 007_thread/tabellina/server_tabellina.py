from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def server_tabellina(conn, addr):
    while conn:
        msg = conn.recv(4096).decode('utf-8')
        #se ricevo exit chiudo la connessione con quel client
        if msg.upper() == "EXIT":
            print(f"Chiusura connessione con {addr}")
            conn.send(msg.encode('utf-8'))
            conn.close()
            break
        else:
            try:
                num_tabellina = int(msg)
                print(f"Eseguo la tabellina del {num_tabellina}...")
                #per 11 volte ciclo e invio il calcolo della tabellina
                for i in range(0,11):
                    ris = num_tabellina*i
                    print(f" {num_tabellina} * {i} = {ris}")
                    conn.sendall(str(ris).encode("utf-8"))
                    time.sleep(2)
            except:
                print("Error")
                conn.send("Error".encode("utf-8"))

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Connesso con {addr}.")

        t = threading.Thread(target=server_tabellina, args=(conn, addr))
        t.start()

        
if __name__ == "__main__":
    main()

