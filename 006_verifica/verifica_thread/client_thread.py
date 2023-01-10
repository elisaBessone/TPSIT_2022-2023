from socket import socket, AF_INET, SOCK_STREAM
from file import File
from comandi import Comandi
BUFFER_SIZE = 4096

def run_client(host, port, comando):
    receiver = ((host, port))
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        comando = input("Inserisci il comando>> ")
        print(f"COMANDO>> {comando}")

        if comando == Comandi.SALVA:
            nome_utente, contenuto = File.valori_input()
            invio_server = (f"{comando}; {nome_utente}; {contenuto}")
            print(f"INVIO AL SERVER>> {invio_server}")
            s.send(invio_server.encode('utf-8'))
            
        elif comando == Comandi.LEGGI:                
            s.send(comando.encode('utf-8'))
            primo_elemento_lista = s.recv(BUFFER_SIZE).decode('utf-8')
            print(primo_elemento_lista)

        elif comando == Comandi.ESCI:
            print("TERMINO IL PROGRAMMA.")

if __name__ == '__main__':
    nome_file = "confClient.txt"
    host, port, comando = File.leggiFile(nome_file)
    print (host, port, comando)
    run_client(host, port, comando)

    