from socket import socket, AF_INET, SOCK_STREAM
import threading
import time
from my_class import MyClassThread


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Connesso con {addr}.")

        t = MyClassThread(conn)

        t.start()

        
if __name__ == "__main__":
    main()