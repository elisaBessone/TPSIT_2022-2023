from socket import socket, AF_INET, SOCK_STREAM
BUFFER_SIZE = 4096


def input_value():
    port_local = int(input("Inserire la porta locale> "))
    host_server = input("Inserire l'indirizzo del server> ")
    port_server = int(input("Inserire la porta del server> "))

    return port_local, (host_server, port_server)

def ricezione(socket_address):
    with socket(AF_INET, SOCK_STREAM) as s:
        #rimango in ascolto su tutte le interfacce di disponibili
        #s.bind(("0.0.0.0", port_local))
        print(socket_address)
        s.bind((socket_address))
        s.listen()
  
        client, address = s.accept()
        print("Server in ascolto...")
        msg = client.recv(BUFFER_SIZE)
        print(f"Richiesta avvenuta dal server >> {msg}")

        #decodifico e splitto
        messaggio = msg.decode("utf-8")
        messaggio = messaggio.split(" ")


        print(f"Messaggio splittato > {messaggio[1]}")
        richiesta = (messaggio[1].split("/"))[1]
        
        richiesta = richiesta + ".json"
        print(richiesta)

        return richiesta

def richiesta_http(richiesta, socket_address):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(socket_address)
        #richiesta = richiesta.encode("utf-8")
        
        percorso = f"GET /{richiesta} HTTP/1.1\n\n"
        print(f"PERCORSO>> {percorso.encode('utf-8')}")
        percorso = percorso.encode('utf-8')
        s.sendall(percorso)
    
        return s.recv(BUFFER_SIZE)

        


def server(socket_local, socket_server):
    
    richiesta = ricezione(socket_local)
    print(f"richiesta socket local >> {richiesta}")
    msg = richiesta_http(richiesta, socket_server)
    print(f"MESSAGGIO RICEVUTO --> \n{msg}\n------------------")




    """richiesta = ricezione(socket_server)
    print(f"richiesta socket server >> {richiesta}")"""
    





if __name__ == '__main__':
    print("Inizio programma>> ")
    port_local, socket_server = input_value()
    socket_local = ("0.0.0.0", port_local)
    server(socket_local, socket_server)



"""server 
bind listen accep
recv http
prendo percorso
"""