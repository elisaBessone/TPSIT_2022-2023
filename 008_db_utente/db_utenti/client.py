from socket import socket, AF_INET, SOCK_STREAM

def controlloComando():
    c = input("Inserire il comando (login - signup) >> ")
    if c.upper() != "SIGNUP" and c.upper() != "LOGIN":
        print("COMANDO ERRATO!!")
        controlloComando()
    else:
        return c

    

def client():
    comando = controlloComando()
    print(comando)
    receiver = ("127.0.0.1", 5000)

    nome_utente = input("Inserisci username>> ")
    psw_utente = input("Inserisci password>> ")
    

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        msg = f"{comando};{nome_utente};{psw_utente}"
        s.sendall(msg.encode("utf-8"))

        conferma = s.recv(4096)
        conferma = conferma.decode("utf-8")

        print(conferma)

        if conferma == "Login avvenuto.":
            stringa = input("Inserisci la stringa da ricercare nell'elenco degli username>>")

            s.sendall(stringa.encode("utf-8"))
            username = s.recv(1024).decode("utf-8")

            print(username)

if __name__ == "__main__":
    client()


   