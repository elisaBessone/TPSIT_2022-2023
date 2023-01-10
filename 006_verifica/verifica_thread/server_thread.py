from socket import socket, AF_INET, SOCK_STREAM
from file import File
from comandi import Comandi
#dimensione del buffer
BUFFER_SIZE = 4096
from my_thread import ThreadComandi

def run_server(host, port):
    #mi connetto al socket tramite i parametri presi da file
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("server listen...")

        #accetto più connessioni. se viene inviato il messaggio esci il server finsice di funzionare.
        while True:
            conn, addr = s.accept()
            print(f"Connesso con {addr}.")

            t = ThreadComandi(conn, lista)
            t.start()




if __name__ == "__main__":
    lista = []
    nome_file = "confServer.txt"
    host, port = File.leggiFile(nome_file)
    run_server(host, port)