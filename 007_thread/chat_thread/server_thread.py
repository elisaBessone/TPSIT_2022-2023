from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def server(conn, addr):
    while conn:
        msg = conn.recv(4096).decode('utf-8')

        if msg.upper() == "EXIT":
            print(f"Chiusura connessione con {addr}")
            conn.send(msg.encode('utf-8'))
            conn.close()
            break
        else:
            try:
                result = eval(msg)   #esegue una stringa ricevuta se ci sono dei comandi funzionanti
                print(f"Risultato {msg}: {result}")
                conn.sendall(str(result).encode("utf-8"))
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

        t = threading.Thread(target=server, args=(conn, addr))
        t.start()

        
if __name__ == "__main__":
    main()