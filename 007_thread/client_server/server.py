from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Connesso con {addr}.")

        msg = conn.recv(4096).decode('utf-8')
        result = eval(msg)   #esegue una stringa ricevuta se ci sono dei comandi funzionanti
        print(result)
        time.sleep(2)
        conn.sendall(("ricevuto".encode('utf-8')))

if __name__ == "__main__":
    main()